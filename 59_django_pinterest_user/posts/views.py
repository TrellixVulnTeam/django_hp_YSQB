from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .forms import PostForm
from .models import Post
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }
    return render(request, 'posts/index.html', context)

@login_required
@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES ) # File은 따로 저장되기 때문에, File 도 추가해줘야한다.
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:detail', post.pk)
    else:
        form = PostForm()

    context = {
        'form': form,
    }
    return render(request, 'posts/form.html', context)


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
    return render(request, 'posts/form.html', context)

def delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('posts:index')



def comment_create(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect('posts:detail', post.pk)