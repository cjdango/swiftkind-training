import json

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import QueryDict, HttpResponse, HttpResponseRedirect
from django.forms.models import model_to_dict
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

from .models import Board, Card, BoardInvitation
from .forms import CreateBoardForm, CreateListForm


class BoardInvitationEditView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        board = Board.objects.get(pk=kwargs.get('board_pk'))
        invitation = get_object_or_404(BoardInvitation, frm=board, to=self.request.user)
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
        board.delete()
        return HttpResponse(
            json.dumps({
                'deleted': model_to_dict(board),
                'redirect': reverse('boards:home')
            }),
            content_type='application/json'
        )

    def get_response(self, request, form=None):
        if form is None:
            form = self.form_class()

        return render(request, self.template_name, {
            'form': form,
            'boards': self.request.user.board_set.all()
        })


class BoardDetailView(LoginRequiredMixin, View):
    template_name = 'boards/board_detail.html'
    form_class = CreateListForm

    def get(self, request, *args, **kwargs):
        return self.get_response(request, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            board = form.save(commit=False)
            board.board = get_object_or_404(Board, pk=kwargs.get('pk'))
            board.save()
            return redirect(self.request.path_info)

        return self.get_response(request, form, **kwargs)

    def delete(self, request, *args, **kwargs):
        body = QueryDict(request.body)
        board = self.request.user.board_set.get(pk=kwargs.get('pk'))
        lst = board.list_set.get(pk=body.get('pk'))

        lst.delete()
        return HttpResponse(
            json.dumps({
                'deleted': model_to_dict(lst),
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
            'board': get_object_or_404(Board, members=self.request.user, pk=kwargs.get('pk'))
        })


class CardListView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        body = QueryDict(request.body)
        board = self.request.user.board_set.get(pk=kwargs.get('board_pk'))
        lst = board.list_set.get(pk=kwargs.get('list_pk'))
        card = Card(title=body.get('title'), lst=lst)
        card.save()

        return HttpResponse(
            json.dumps({
                'created': model_to_dict(card),
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
        card.delete()

        return HttpResponse(
            json.dumps({
                'deleted': model_to_dict(card),
                'redirect': reverse('boards:board_detail',
                                    args=[str(board.pk)])
            }),
            content_type='application/json'
        )