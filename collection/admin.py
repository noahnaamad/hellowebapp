# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

#import model
from collection.models import Post

#automated slug creation
class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

# Register your models here.
admin.site.register(Post, PostAdmin)
