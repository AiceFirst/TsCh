# -*- coding: utf-8 -*-
from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from django.utils import timezone
from datetime import datetime, timedelta

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'picha.settings')
app = Celery('picha')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


@app.task(bind=True)
def form_view(self):
    self.Post.objects.filter(published_date__gte=(datetime.now() - timedelta(days=1))).delete()