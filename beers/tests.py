from django.test import TestCase
from beers.models import Post
from django.contrib.auth.models import User
from datetime import datetime, timedelta
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TsCh.settings")

class PostTestCase(TestCase):
      def setUp(self):
                    me = User(username='tete', password='123')
                    me.save()
                    Post.objects.create(author=me, title='Truly Delete', text='Delete Dis', published_date=datetime(2012, 3, 1, 10, 0))

      def test_animals_can_speak(self):
           post = Post.objects.get(title='Truly Delete')
           post.publish()
           Post.objects.filter(created_date__gte=(datetime.now() - timedelta(days=1))).delete()
           self.assertEqual(Post.objects.all(), [])
# Create your tests here.
