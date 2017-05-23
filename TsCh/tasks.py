# -*- coding: utf-8 -*-
from __future__ import absolute_import
from celery import Celery
from celery.task import periodic_task
from celery.app import task
from django.utils import timezone
from datetime import datetime, timedelta
from . import settings
import sqlite3
#from beers.models import Post
from celery.task import task




@task(bind=True, default_retry_delay=300)
def delete_some():
        from beers.models import Post
        post = Post.objects.all()
        post.filter(created_date__gte=(datetime.now() - timedelta(days=1))).delete()
