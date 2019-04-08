from django.db import models
from django.contrib.auth import get_user_model


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
