import json

from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
    get_list_or_404
)
from django.urls import reverse, reverse_lazy
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import QueryDict, HttpResponse, HttpResponseRedirect
from django.forms.models import model_to_dict
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

from .models import (
    Board,
    Card,
    BoardInvitation,
    CardComment,
    BoardActivityLog,
    List,
)
from .forms import CreateBoardForm, CreateListForm


class BoardActivityLogView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        board = get_object_or_404(
            Board,
            pk=kwargs.get('pk'),
            members=self.request.user)
        logs_queryset = BoardActivityLog.objects.filter(
            board=board).order_by('-pk')

        logs_list = []

        for log in logs_queryset:
            logs_list.append({
                'actor': log.actor.username,
                'verb': log.verb,
                'target': str(log.target),
                'content': str(log.action),
                'content_type': log.action.__class__.__name__
            })

        return HttpResponse(
            json.dumps(logs_list),
            content_type='application/json'
        )


class BoardInvitationEditView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        board = Board.objects.get(pk=kwargs.get('board_pk'))
        invitation = get_object_or_404(
            BoardInvitation, frm=board, to=self.request.user)
        invitation.accept(request)

        return redirect(reverse_lazy(
            'boards:board_detail', args=[str(board.pk)]))


class BoardInvitationListView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        body = QueryDict(request.body)
        board = self.request.user.board_set.get(pk=kwargs.get('board_pk'))
        to = get_object_or_404(get_user_model(), email=body.get('to'))

        BoardInvitation.objects.get_or_create(frm=board, to=to)

        send_mail(
            'Board Invitation',
            'Accept?: http://127.0.0.1:8000' +
            reverse('boards:invite_edit', args=[str(board.pk)]),
            'trello.clone@example.com',
            [to.email],
            fail_silently=False,
        )

        invitation = {
            'from': board.owner.email,
            'board': board.pk,
            'to': to.email
        }

        return HttpResponse(
            json.dumps({
                'invitation': invitation,
                'redirect': reverse('boards:board_detail',
                                    args=[str(board.pk)])
            }),
            content_type='application/json'
        )


class BoardListView(LoginRequiredMixin, View):
    template_name = 'boards/board_list.html'
    form_class = CreateBoardForm

    def get(self, request, *args, **kwargs):
        return self.get_response(request)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            board = form.save(commit=False)
            board.owner = request.user
            board.save()
            board.members.add(request.user)
            form.save_m2m()
            return redirect(self.request.path_info)

        return self.get_response(request, form)

    def delete(self, request, *args, **kwargs):
        body = QueryDict(request.body)
        board = self.request.user.board_set.get(pk=body.get('pk'))
        board.is_archived = True
        board.save()
        return HttpResponse(
            json.dumps({
                'archived': model_to_dict(board),
                'redirect': reverse('boards:home')
            }),
            content_type='application/json'
        )

    def get_response(self, request, form=None):
        if form is None:
            form = self.form_class()

        return render(request, self.template_name, {
            'form': form,
            'boards': self.request.user.board_set.filter(is_archived=False)
        })


class BoardDetailView(LoginRequiredMixin, View):
    template_name = 'boards/board_detail.html'
    form_class = CreateListForm

    def get(self, request, *args, **kwargs):
        return self.get_response(request, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            lst = form.save(commit=False)
            lst.board = get_object_or_404(Board, pk=kwargs.get('pk'))
            lst.save()

            BoardActivityLog.objects.create(
                board=lst.board,
                actor=self.request.user,
                verb='created',
                target=lst.board,
                action=lst)

            for member in lst.board.members.exclude(email=request.user):
                send_mail(
                    'Board activity',
                    f'{request.user.username} created {lst} list in {lst.board} board.',
                    'trello.clone@example.com',
                    [member.email],
                    fail_silently=False,
                )

            return redirect(self.request.path_info)

        return self.get_response(request, form, **kwargs)

    def delete(self, request, *args, **kwargs):
        body = QueryDict(request.body)
        board = self.request.user.board_set.get(pk=kwargs.get('pk'))
        lst = board.list_set.get(pk=body.get('pk'))

        lst.is_archived = True
        lst.save()
        return HttpResponse(
            json.dumps({
                'archived': model_to_dict(lst),
                'redirect': reverse('boards:board_detail',
                                    args=[str(board.pk)])
            }),
            content_type='application/json'
        )

    def get_response(self, request, form=None, **kwargs):
        if form is None:
            form = self.form_class()

        return render(request, self.template_name, {
            'form': form,
            'board': get_object_or_404(Board, members=self.request.user,
                                       pk=kwargs.get('pk'), is_archived=False)
        })


class CardListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        board = self.request.user.board_set.get(pk=kwargs.get('board_pk'))
        lst = board.list_set.get(pk=kwargs.get('list_pk'))
        card = lst.card_set.get(pk=request.GET.get('pk'))
        comments = list(card.cardcomment_set.values())

        for comment in comments:
            frm_user = get_user_model().objects.get(
                pk=comment['frm_id'])
            comment['frm_email'] = frm_user.email
            comment['frm_username'] = frm_user.username

        return HttpResponse(
            json.dumps({
                'card': model_to_dict(card),
                'card_comments': comments,
                'redirect': reverse('boards:board_detail',
                                    args=[str(board.pk)])
            }),
            content_type='application/json'
        )

    def post(self, request, *args, **kwargs):
        body = QueryDict(request.body)
        board = self.request.user.board_set.get(pk=kwargs.get('board_pk'))
        lst = board.list_set.get(pk=kwargs.get('list_pk'))
        card = Card(title=body.get('title'), lst=lst)
        card.save()

        BoardActivityLog.objects.create(
            board=board,
            actor=self.request.user,
            verb='created',
            target=lst,
            action=card)

        for member in lst.board.members.exclude(email=request.user):
            send_mail(
                'Board activity',
                f'{request.user.username} created {card} card in {lst} list, {board} board.',
                'trello.clone@example.com',
                [member.email],
                fail_silently=False,
            )

        return HttpResponse(
            json.dumps({
                'created': model_to_dict(card),
                'redirect': reverse('boards:board_detail',
                                    args=[str(board.pk)])
            }),
            content_type='application/json'
        )

    def put(self, request, *args, **kwargs):
        body = QueryDict(request.body)
        board = self.request.user.board_set.get(pk=kwargs.get('board_pk'))
        lst = board.list_set.get(pk=kwargs.get('list_pk'))
        card = lst.card_set.get(pk=body.get('pk'))

        comment_context = body.get('comment')
        tags = [s for s in comment_context.split() if "@" in s]

        for tag in tags:
            try:
                get_user_model().objects.get(username=tag[1:])
                styled_tag = f'<span class="text-info">{tag}</span>'
                comment_context = comment_context.replace(tag, styled_tag)
            except get_user_model().DoesNotExist:
                pass

        comment = CardComment.objects.create(
            comment=comment_context, card=card, frm=self.request.user)

        BoardActivityLog.objects.create(
            board=board,
            actor=self.request.user,
            verb='said',
            target=card,
            action=comment)

        for member in lst.board.members.exclude(email=request.user):
            send_mail(
                'Board activity',
                f'{request.user.username} said {comment_context} in {card} card, {lst} list, {board} board.',
                'trello.clone@example.com',
                [member.email],
                fail_silently=False,
            )

        return HttpResponse(
            json.dumps({
                'commented': model_to_dict(comment),
                'redirect': reverse('boards:board_detail',
                                    args=[str(board.pk)])
            }),
            content_type='application/json'
        )

    def delete(self, request, *args, **kwargs):
        body = QueryDict(request.body)
        board = self.request.user.board_set.get(pk=kwargs.get('board_pk'))
        lst = board.list_set.get(pk=kwargs.get('list_pk'))
        card = lst.card_set.get(pk=body.get('pk'))
        card.is_archived = True
        card.save()

        return HttpResponse(
            json.dumps({
                'archived': model_to_dict(card),
                'redirect': reverse('boards:board_detail',
                                    args=[str(board.pk)])
            }),
            content_type='application/json'
        )


class CardCommentView(LoginRequiredMixin, View):
    def delete(self, request, *args, **kwargs):
        body = QueryDict(request.body)
        comment = get_object_or_404(
            CardComment,
            frm=self.request.user,
            pk=body.get('pk'))
        comment.is_archived = True
        comment.save()

        return HttpResponse(
            json.dumps({
                'archived': model_to_dict(comment)
            }),
            content_type='application/json'
        )


@login_required
def set_list_order(request, *args, **kwargs):
    if request.method == 'POST':
        board = get_object_or_404(
            Board,
            pk=kwargs.get('board_pk'),
            members=request.user,
        )

        body = QueryDict(request.body)
        order = body.getlist('order[]')

        for idx, pos in enumerate(order):
            lst = get_object_or_404(List, pk=pos, board=board)
            lst.position = idx + 1
            lst.save()

        return HttpResponse(
            json.dumps({
                'order_set': 'success'
            }),
            content_type='application/json'
        )


@login_required
def set_card_order(request, *args, **kwargs):
    if request.method == 'POST':
        board = get_object_or_404(
            Board,
            pk=kwargs.get('board_pk'),
            members=request.user,
        )
        lst = get_object_or_404(List, pk=kwargs.get('list_pk'), board=board)

        body = QueryDict(request.body)
        order = body.getlist('order[]')

        for idx, pos in enumerate(order):
            card = get_object_or_404(Card, pk=pos, lst=lst)
            card.position = idx + 1
            card.save()

        return HttpResponse(
            json.dumps({
                'order_set': 'success'
            }),
            content_type='application/json'
        )


@login_required
def set_card_list(request, *args, **kwargs):
    if request.method == 'PUT':
        board = get_object_or_404(
            Board,
            pk=kwargs.get('board_pk'),
            members=request.user,
        )
        lst = get_object_or_404(List, pk=kwargs.get('list_pk'), board=board)

        body = QueryDict(request.body)
        to_list_pk = body.get('to_list_pk')
        card_pk = kwargs.get('card_pk')

        card = get_object_or_404(Card, pk=card_pk, lst=lst)
        to_list = get_object_or_404(List, pk=to_list_pk, board=board)

        card.lst = to_list
        card.save()

        return HttpResponse(
            json.dumps({
                'set_card_list': 'success'
            }),
            content_type='application/json'
        )


@login_required
def set_list_title(request, *args, **kwargs):
    if request.method == 'PUT':
        body = QueryDict(request.body)
        lst = get_object_or_404(
            List, pk=kwargs.get('list_pk'),
            board__pk=kwargs.get('board_pk'),
            board__members=request.user)

        title = body.get('title')
        lst.title = title
        lst.save()

        return HttpResponse(
            json.dumps({
                'set_list_title': 'success'
            }),
            content_type='application/json'
        )


@login_required
def set_card_title(request, *args, **kwargs):
    if request.method == 'PUT':
        body = QueryDict(request.body)
        card = get_object_or_404(
            Card, pk=kwargs.get('card_pk'),
            lst__pk=kwargs.get('list_pk'),
            lst__board__pk=kwargs.get('board_pk'),
            lst__board__members=request.user)

        title = body.get('title')
        card.title = title
        card.save()

        return HttpResponse(
            json.dumps({
                'set_card_title': 'success'
            }),
            content_type='application/json'
        )


@login_required
def leave_board(request, *args, **kwargs):
    if request.method == 'POST':
        board = get_object_or_404(
            Board, pk=kwargs.get('pk'),
            members=request.user)

        if board.owner == request.user:
            board.is_archived = True
            board.save()
            return HttpResponse(
                json.dumps({
                    'archived_board': 'success',
                    'redirect': reverse('boards:home')
                }),
                content_type='application/json'
            )

        board.members.remove(request.user)

        return HttpResponse(
            json.dumps({
                'leave_board': 'success',
                'redirect': reverse('boards:home')
            }),
            content_type='application/json'
        )


@login_required
def fetch_archived_lists(request, *args, **kwargs):
    if request.method == 'GET':
        archived_lists = get_list_or_404(
            List,
            board__pk=kwargs.get('board_pk'),
            board__members=request.user,
            is_archived=True
        )

        for idx, lst in enumerate(archived_lists):
            archived_lists[idx] = model_to_dict(lst)

        return HttpResponse(
            json.dumps({
                'archived_lists': archived_lists
            }),
            content_type='application/json'
        )


@login_required
def fetch_archived_cards(request, *args, **kwargs):
    if request.method == 'GET':
        archived_cards = get_list_or_404(
            Card,
            lst__board__pk=kwargs.get('board_pk'),
            lst__board__members=request.user,
            is_archived=True
        )

        for idx, card in enumerate(archived_cards):
            archived_cards[idx] = model_to_dict(card)

        return HttpResponse(
            json.dumps({
                'archived_cards': archived_cards
            }),
            content_type='application/json'
        )


@login_required
def unarchive_list(request, *args, **kwargs):
    if request.method == 'PUT':
        body = QueryDict(request.body)
        lst = get_object_or_404(
            List,
            pk=body.get('pk'),
            board__pk=kwargs.get('board_pk'),
            board__members=request.user
        )
        lst.is_archived = False
        lst.save()

        return HttpResponse(
            json.dumps({
                'unarchive_list': 'success'
            }),
            content_type='application/json'
        )


@login_required
def unarchive_card(request, *args, **kwargs):
    if request.method == 'PUT':
        body = QueryDict(request.body)
        card = get_object_or_404(
            Card,
            pk=body.get('pk'),
            lst__board__pk=kwargs.get('board_pk'),
            lst__board__members=request.user
        )
        card.is_archived = False
        card.save()

        return HttpResponse(
            json.dumps({
                'unarchive_card': 'success'
            }),
            content_type='application/json'
        )
