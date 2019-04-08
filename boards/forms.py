from django import forms

from .models import Board, List, Card


class CreateBoardForm(forms.ModelForm):

    class Meta:
        model = Board
        fields = ('title',)


class CreateListForm(forms.ModelForm):

    class Meta:
        model = List
        fields = ('title',)


class CreateCardForm(forms.ModelForm):

    class Meta:
        model = Card
        fields = ('title',)
