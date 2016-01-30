from django.shortcuts import render
from TsCh.settings import MEDIA_ROOT, MEDIA_URL
from django.utils import timezone
from django.shortcuts import render_to_response
from .models import Post, BadWords
from .forms import PostForm


# Create your views here.


def post_list(request):
  ##for element in BadWords.bwords:
   ##  if Post.text == element:
    ##  Post.text = '***'
  posts = Post.objects.order_by('published_date')
  return render_to_response('post_list.html', {'posts': posts, 'images': MEDIA_URL, 'media_root': MEDIA_ROOT})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
    else:
        form = PostForm()

    return render_to_response('post_list.html', {'form': form})
