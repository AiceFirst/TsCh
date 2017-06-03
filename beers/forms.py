# -*- coding: utf-8 -*-
import os

from django import forms
from beers.models import Post

os.environ['DJANGO_SETTINGS_MODULE'] = 'TsCh.settings'


class PostForm(forms.ModelForm):
    class Meta:
            model = Post
            fields = ('text',)
            template_name = 'post_list.html'

