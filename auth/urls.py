# -*- coding: utf-8 -*-
from django.conf.urls import url
from auth import views
from django.contrib.auth.views import login,logout


urlpatterns = [
    url(r'^login/$', login, {'template_name': 'login.html', 'redirect_field_name': r'^$'}, name='login'),
    url(r'^register/$', views.RegisterFormView.as_view()),
    url(r'^logout2/$', logout, {'template_name': 'logout.html', 'redirect_field_name': r'^$'}, name='auth_logout'),
    ]


