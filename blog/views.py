from django.views.generic import DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, resolve
from django.shortcuts import render, redirect, get_object_or_404
from django.forms.models import model_to_dict
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Post
from .forms import NewPostForm


class BlogListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        return render(request, 'blog/home.html', context={'posts': posts})


class BlogDetailView(View):
    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs.get('pk'))
        return render(request, 'blog/post_detail.html', context={'post': post})


class BlogCreateView(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        form = NewPostForm()
        return render(request, 'blog/post_new.html', context={'form': form})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = NewPostForm(request.POST, request.FILES)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(post)

        return render(request, 'blog/post_new.html', context={'form': form})


class BlogUpdateView(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        post = get_object_or_404(
            Post, pk=kwargs.get('pk'), author=request.user)
        
        form = NewPostForm(instance=post)
        return render(request, 'blog/post_edit.html', context={'form': form})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        instance = get_object_or_404(
            Post, pk=kwargs.get('pk'), author=request.user)
        form = NewPostForm(request.POST, request.FILES, instance=instance)

        if form.is_valid():
            post = form.save()
            return redirect(post)

        return render(request, 'blog/post_edit.html',
                      context={'form': form})


class BlogDeleteView(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        post = get_object_or_404(
            Post, pk=kwargs.get('pk'), author=request.user)

        return render(request, 'blog/post_delete.html', context={'post': post})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        post = get_object_or_404(
            Post, pk=kwargs.get('pk'), author=request.user)
            
        post.delete()
        return redirect(reverse_lazy('home'))
