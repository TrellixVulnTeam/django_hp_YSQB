from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from django.views.decorators.http import require_POST
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .forms import CustomUserChangeForm
from django.contrib.auth.decorators import login_required



# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index') # 로그인이 되어있는 상태라면 로그인 로직에 접근할 수 없도록 처리


    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 세션 만들어 준다.
            auth_login(request, form.get_user()) # 이름이 둘다 login이면 안됨
            return redirect(request.GET.get('next') or 'articles:index') # 로그인하고 어디로 갈지 정해져 있다면 이동하도록 변경
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@require_POST
def logout(request):
    auth_logout(request)
    return redirect('articles:index')


def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index') # 로그인이 되어있는 상태라면 로그인 로직에 접근할 수 없도록 처리

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
    return redirect('articles:index')

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)