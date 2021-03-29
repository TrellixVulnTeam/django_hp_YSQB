from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST
from django.contrib.auth import get_user_model
# Create your views here.
def login(request):
    if request.method == 'POST':
        # 로그인 처리하며
        form = AuthenticationForm(request, request.POST) 
        if form.is_valid():
            # 이제 로그인을 시켜주면 되는데 로직이 장고에 있음
            auth_login(request, form.get_user()) # 로그인 할때 request와 유저정보가 필요함
            return redirect('posts:index') 
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/form.html', context)

def profile(request, pk):
    User = get_user_model() # 현재 User 모델
    user_info = User.objects.get(pk=pk)
    context = {
        'user_info': user_info
    }
    return render(request, 'accounts/profile.html', context)

@require_POST
def logout(request):
    auth_logout(request)
    return redirect('accounts:login')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/form.html', context)

