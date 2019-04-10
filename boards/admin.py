from django.contrib import admin

from .models import (
    Board,
    List,
    Card,
    BoardInvitation,
    CardComment,
    BoardActivityLog,
)

admin.site.register(BoardInvitation)
admin.site.register(BoardActivityLog)
admin.site.register(Board)
admin.site.register(List)
admin.site.register(Card)
admin.site.register(CardComment)
