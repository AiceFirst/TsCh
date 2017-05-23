from django.http.response import HttpResponseForbidden, Http404
from django.shortcuts import render
from TsCh.settings import MEDIA_ROOT, MEDIA_URL
from django.utils import timezone
from django.shortcuts import render_to_response, HttpResponseRedirect, get_object_or_404, redirect
from beers.forms import PostForm
from beers.models import Post, BadWords
from django.contrib.auth.models import User



# Create your views here.

def post_list(request):
    fl = False
    if request.user.is_authenticated():
            fl = True
    if request.method == "POST":
        form = PostForm(request.POST)
        if request.user.is_authenticated():
            if form.is_valid():
                post = form.save(commit=False)
               # for bword in BadWords.objects.get().bwords:
                #    post.text.replace(bword, "".join(['*', bword[1:-1], '*']))
                post.author = request.user
                post.title = '...'
                post.published_date = timezone.now()
                post.save()
                return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/auth/login/')
    else:
            form = PostForm()
    posts = Post.objects.order_by('published_date')
    top = top_count(request)
    return render_to_response('post_list.html', {'posts': posts, 'authed': fl, 'top': top, 'form': form, 'images': MEDIA_URL, 'media_root': MEDIA_ROOT})

def post_detail(request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'post_detail.html', {'post': post})


from django.views.generic.edit import DeleteView # this is the generic view
from django.core.urlresolvers import reverse_lazy


def user_have_perms(request, pk):
    post = get_object_or_404(Post, pk=pk)
    fl = False
    if request.user.is_authenticated():
        if request.user == post.author:
            fl = True
    return fl



class NoteDelete(DeleteView):
    model = Post
    template_name = 'delete_massage.html'
    success_url = reverse_lazy('post_list')

    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(NoteDelete, self).get_object()
        if not user_have_perms(self.request, obj.id):
            raise Http404
        return obj


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

from django.db.models import Count
from django.contrib.auth.models import User


def top_count(request):

    top_men = User.objects.annotate(post_times=Count('post')).order_by('-post_times')[:5]
    top_authors = ''
    for i in top_men:
     top_authors = top_authors + str(i)+', '
    top_authors = top_authors[:-2]
    return top_authors


def post_cruser(request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = post.author.username
        return render(request, 'cruser.html', {'form': form}) #ToDo chec the authors and bring them from db!!



