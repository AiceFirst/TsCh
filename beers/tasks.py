# -*- coding: utf-8 -*-
 #from celery import Celery
# from celery.task import periodic_task
# from celery.app import task
# from django.utils import timezone
# from datetime import datetime, timedelta
#
# app = Celery('tasks')
# app.conf.task_serializer = 'json'
# CELERY_BROKER_URL = 'django://'
# CELERY_ACCEPT_CONTENT = ['pickle', 'json']
#
# @app.task(name='sum-of-two-numbers')
# def add(x, y):
#     return x + y
#
# @periodic_task(name='Delete-old-posts', run_every=10)
# def delete_some():
#     from beers.models import Post
#     Post.objects.filter(published_date__gte=(datetime.now() - timedelta(days=1))).delete()