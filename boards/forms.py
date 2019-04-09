from django import forms

from .models import Board, List, Card


class CreateBoardForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Card title here...'
        })
    )

    def __init__(self, *args, **kwargs):
        super(CreateBoardForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = ''

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
        form_show_labels = False
