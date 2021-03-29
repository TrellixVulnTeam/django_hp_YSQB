from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .forms import PostForm
from .models import Post

# Create your views here.
def index(request):
    pass
    # Q1

@require_http_methods(['GET', 'POST'])
def create(request):
    pass
    # Q2


def detail(request, pk):
    post = Post.objects.get(pk=pk)

    context = {
        'post': post,
    }

    return render(request, 'posts/detail.html', context)


def update(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:detail', post.pk)
    else:
        form = PostForm(instance=post)
    context = {
        'form': form,
    }
    return render(request, 'posts/update.html', context)