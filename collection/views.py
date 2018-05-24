# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from collection.models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {
    'posts': posts,
    })
