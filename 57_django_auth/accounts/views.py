from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import (
    UserCreationForm, 
    AuthenticationForm,
    UserChangeForm,
    PasswordChangeForm,
    )
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/form.html', context)


def login(request):
    if request.user.is_authenticated:
        messages.add_message(request, messages.WARNING, '이미 로그인 되어 있는 유저입니다.')
        return redirect('accounts:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        # form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user()) # 로그인 성공
            messages.add_message(request, messages.SUCCESS, '로그인이 성공 했습니다.')
            return redirect('accounts:index')
        messages.add_message(request, messages.error, '로그인이 실패 했습니다.')

    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/form.html', context)


def logout(request):
    auth_logout(request)
    return redirect('accounts:login')


def index(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'accounts/index.html', context)

def profile(request, username):
    user = get_object_or_404(User, username=username)
    context = {
        'user_info': user,
    }
    return render(request, 'accounts/profile.html', context)

def delete(request):
    request.user.delete()
    return redirect('accounts:index')


def update(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            message.success(request, '수정 완료 되었습니다!!')
            return redirect('accounts:profile', request.user.username)
    else:
        form = UserChangeForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/form.html', context)
    
def pw_update(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, '비밀번호가 성공적으로 변경되었습니다!')
            return redirect('accounts:profile', request.user.username)
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/form.html', context)