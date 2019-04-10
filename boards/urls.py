from django.urls import path

from boards.models import Card
from .views import (
    BoardListView,
    BoardDetailView,
    BoardInvitationListView,
    BoardInvitationEditView,
    CardListView,
    CardCommentView
)

app_name = 'boards'
urlpatterns = [
    path('', BoardListView.as_view(), name='home'),
    path('boards/<int:pk>/', BoardDetailView.as_view(), name='board_detail'),
    path('boards/<int:board_pk>/lists/<int:list_pk>/cards/',
         CardListView.as_view(), name='card_list'),
    path('boards/<int:board_pk>/lists/<int:list_pk>/' \
         'cards/<int:card_pk>/comments/',
         CardCommentView.as_view(), name='comment_view'),
    path('boards/<int:board_pk>/invites/new/',
         BoardInvitationListView.as_view(), name='invite_new'),
    path('boards/<int:board_pk>/invites/accept/',
         BoardInvitationEditView.as_view(), name='invite_edit'),
]
