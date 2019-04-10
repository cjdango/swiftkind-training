from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Board(models.Model):
    title = models.CharField(max_length=50)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='board_owned_set')
    members = models.ManyToManyField(
        get_user_model(), related_name='board_set')

    def __str__(self):
        return self.title


class BoardActivityLog(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    actor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    verb = models.CharField(max_length=20)

    target_content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        related_name='activiylog_target')

    tartget_object_id = models.PositiveIntegerField()
    target = GenericForeignKey(
        'target_content_type',
        'tartget_object_id')

    action_content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        related_name='activiylog_action')

    action_object_id = models.PositiveIntegerField()
    action = GenericForeignKey(
        'action_content_type',
        'action_object_id')


class BoardInvitation(models.Model):
    frm = models.ForeignKey(Board, on_delete=models.CASCADE)
    to = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.frm.title} -> {self.to.email}'

    def accept(self, request):
        self.frm.members.add(request.user)
        self.delete()


class List(models.Model):
    title = models.CharField(max_length=50)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Card(models.Model):
    title = models.CharField(max_length=50)
    lst = models.ForeignKey(List, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class CardComment(models.Model):
    comment = models.CharField(max_length=50)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    frm = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
