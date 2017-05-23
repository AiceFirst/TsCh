# -*- coding: utf-8 -*-
import os
from django.conf import settings
from django.utils import timezone
from datetime import datetime, timedelta


# Using a string here means the worker will not have to
# pickle the object when using Windows.





@app.task(bind=True)
def form_view(self):
    self.Post.objects.filter(published_date__gte=(datetime.now() - timedelta(days=1))).delete()

@app.task(bind=True)
def delete_some():
    from beers.models import Post
    Post.objects.filter(published_date__gte=(datetime.now() - timedelta(days=1))).delete()
