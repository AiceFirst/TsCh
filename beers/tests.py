from django.test import TestCase
from beers.models import Post
from django.contrib.auth.models import User
from datetime import datetime, timedelta
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TsCh.settings")




me = User.objects.get(username='tete')
Post.objects.create(author=me, title='Truly Delete', text='Delete Dis', published_date=datetime(2012, 3, 1, 10, 0))
post = Post.objects.get(title='Truly Delete')
post.publish()
Post.objects.filter(created_date__gte=(datetime.now() - timedelta(days=1))).delete()
# Create your tests here.
