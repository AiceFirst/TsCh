# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html', 'redirect_field_name': r'^$'}),
    url(r'^register/$', views.RegisterFormView.as_view()),
]


