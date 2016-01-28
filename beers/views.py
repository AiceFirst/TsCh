from django.shortcuts import render
from TsCh.settings import MEDIA_ROOT, MEDIA_URL
from django.utils import timezone
from django.shortcuts import render_to_response
from .models import Post, BadWords


# Create your views here.


def post_list(request):
  ##for element in BadWords.bwords:
   ##  if Post.text == element:
    ##  Post.text = '***'
  posts = Post.objects.order_by('published_date')
  return render_to_response('post_list.html', {'posts': posts, 'images': MEDIA_URL, 'media_root': MEDIA_ROOT})

