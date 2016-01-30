from django.db import models
from django.utils import timezone
from .tasks import delete_some
from datetime import datetime, timedelta

import re
# Create your models here.
class BadWords(models.Model):
    bwords = models.TextField()

    def __str__(self):
        return str(self.bwords.split(','))


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    delete_some.delay()

    def publish(self):
        self.published_date = timezone.now()
        self.save()



    def __str__(self):
        return self.text


