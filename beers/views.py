from django.shortcuts import render
from TsCh.settings import MEDIA_ROOT, MEDIA_URL
from django.utils import timezone
from django.shortcuts import render_to_response, HttpResponseRedirect,get_object_or_404,redirect
from .models import Post, BadWords
from django.contrib.auth import authenticate, login as auth_login
from .forms import PostForm
from django.contrib.auth.models import Permission, User
from TsCh import settings
from django.contrib.auth.models import User


# Create your views here.


def post_list(request):
  ##for element in BadWords.bwords:
   ##  if Post.text == element:
    ##  Post.text = '***'
    posts = Post.objects.order_by('published_date')
    return render_to_response('post_list.html', {'posts': posts, 'images': MEDIA_URL, 'media_root': MEDIA_ROOT})

def post_detail(request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.title = post.pk
                post.published_date = timezone.now()
                post.save()
                return redirect('beers.views.post_detail', pk=post.pk)
    else:
            form = PostForm()
    return render(request, 'post_list.html', {'form': form})

from django.views.generic.edit import DeleteView # this is the generic view
from django.core.urlresolvers import reverse_lazy
from beers.models import Post

def user_have_perms(request, pk, fl):           ##Todo 1. Тут надо зачекать, что оно возвращает флаг и перейти в пункт 2.
    post = get_object_or_404(Post, pk=pk)
    fl = False
    if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                 if request.user.is_authenticated():
                    if User.get_username == post.author:
                        fl = True
    return fl

from django.contrib.auth.decorators import permission_required


class NoteDelete(DeleteView):
       def somefunc(self):
              if user_have_perms:
                 NoteDelete.model = Post
                 nisan = self.somefunc(model=Post, success_url=reverse_lazy('post_list'), template_name='delete_massage.html')
                 return nisan
              else:
                 return None

def post_edit(request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.published_date = timezone.now()
                post.save()
                return redirect('beers.views.post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'post_edit.html', {'form': form})


