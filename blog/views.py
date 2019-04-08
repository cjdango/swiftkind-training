from django.views.generic import View
from django.urls import reverse_lazy, resolve
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post, Category, Tag
from .forms import NewPostForm


class BlogTagView(View):
    def get(self, request, *args, **kwargs):
        tag = get_object_or_404(Tag, slug=kwargs.get('slug'))
        posts = Post.objects.filter(tag=tag)
        return render(request, 'blog/post_list.html', {'posts': posts})


class BlogCategoryView(View):
    def get(self, request, *args, **kwargs):
        category = get_object_or_404(Category, slug=kwargs.get('slug'))
        posts = Post.objects.filter(category=category)
        return render(request, 'blog/post_list.html', {'posts': posts})


class BlogListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        return render(request, 'blog/post_list.html', {'posts': posts})


class BlogDetailView(View):
    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, slug=kwargs.get('slug'))
        return render(request, 'blog/post_detail.html', {'post': post})


class BlogCreateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = NewPostForm()
        return render(request, 'blog/post_new.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = NewPostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            return redirect(post)

        return render(request, 'blog/post_new.html', {'form': form})


class BlogUpdateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        post = get_object_or_404(
            Post, slug=kwargs.get('slug'), author=request.user)

        form = NewPostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})

    def post(self, request, *args, **kwargs):
        instance = get_object_or_404(
            Post, slug=kwargs.get('slug'), author=request.user)
        form = NewPostForm(request.POST, request.FILES, instance=instance)

        if form.is_valid():
            post = form.save()
            return redirect(post)

        return render(request, 'blog/post_edit.html', {'form': form})


class BlogDeleteView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        post = get_object_or_404(
            Post, slug=kwargs.get('slug'), author=request.user)

        return render(request, 'blog/post_delete.html', {'post': post})

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(
            Post, slug=kwargs.get('slug'), author=request.user)

        post.delete()
        return redirect(reverse_lazy('home'))
