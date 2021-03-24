from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from .forms import CustomUserChangeForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'accounts/index.html', context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/form.html', context)


def login(request):
    if request.user.is_authenticated:
        messages.add_message(request, messages.warning, '이미 로그인 되어 있습니다.')
        return redirect('accounts:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            messages.add_message(request, messages.SUCCESS, '로그인이 성공 했습니다.')
            return redirect('accounts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/form.html', context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:index')

def profile(request, username):
    user = User.objects.get(username=username)
    context = {
        'user': user
    }
    return render(request, 'accounts/profile.html', context)

def delete(request):
    request.user.delete()
    return redirect('accounts:index')

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, '정보 수정이 잘 됐습니다.')
            return redirect('accounts:profile', request.user.username)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/form.html', context)
