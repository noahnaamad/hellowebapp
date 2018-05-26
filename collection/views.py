# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from collection.models import Post
from collection.forms import PostForm

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {
    'posts': posts,
    })

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_detail.html', {
        'post': post,
    })

def edit_post(request, slug):
    post= Post.objects.get(slug=slug)
    form_class = PostForm
    #if the request is coming from a submitted form
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', slug=post.slug)
    #if the request is for an empty form
    else:
        form = form_class(instance=post)

    return render(request, 'posts/edit_post.html', {
        'post': post,
        'form': form,
    })
