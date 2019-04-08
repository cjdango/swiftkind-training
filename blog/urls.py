from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    BlogCategoryView,
    BlogTagView,
)

urlpatterns = [
    path(
        'tag/<slug:slug>/', BlogTagView.as_view(), name="tag"),
    path(
        'category/<slug:slug>/',
        BlogCategoryView.as_view(),
        name="category"),
    path(
        'post/<slug:slug>/delete/',
        BlogDeleteView.as_view(),
        name='post_delete'),
    path('post/<slug:slug>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<slug:slug>/', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
]
