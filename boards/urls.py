from django.urls import path

from boards.models import Card
from .views import (
    BoardListView,
    BoardDetailView,
    BoardInvitationListView,
    BoardInvitationEditView,
    CardListView,
    CardCommentView,
    BoardActivityLogView,
    set_list_order,
    set_card_order,
    set_card_list,
)

app_name = 'boards'
urlpatterns = [
    path('', BoardListView.as_view(), name='home'),
    path('boards/<int:pk>/', BoardDetailView.as_view(), name='board_detail'),
    path('boards/<int:pk>/activity-log/',
         BoardActivityLogView.as_view(), name='activity_log'),
    path('boards/<int:board_pk>/lists/set-order/',
         set_list_order, name='set_list_order'),
    path('boards/<int:board_pk>/lists/<int:list_pk>/cards/set-order/',
         set_card_order, name='set_card_order'),
    path('boards/<int:board_pk>/lists/<int:list_pk>/cards/',
         CardListView.as_view(), name='card_list'),
    path('boards/<int:board_pk>/lists/<int:list_pk>/' +
         'cards/<int:card_pk>/set-list/',
         set_card_list, name='set_card_list'),
    path('boards/<int:board_pk>/lists/<int:list_pk>/' +
         'cards/<int:card_pk>/comments/',
         CardCommentView.as_view(), name='comment_view'),
    path('boards/<int:board_pk>/invites/new/',
         BoardInvitationListView.as_view(), name='invite_new'),
    path('boards/<int:board_pk>/invites/accept/',
         BoardInvitationEditView.as_view(), name='invite_edit'),
]
