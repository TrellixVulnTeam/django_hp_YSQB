from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

# Create your views here.
def login(request):
    if request.method == 'POST':
        # 로그인 처리하며
        form = AuthenticationForm(request, request.POST) 
        if form.is_valid():
            # 이제 로그인을 시켜주면 되는데 로직이 장고에 있음
            auth_login(request, form.get_user) # 로그인 할때 request와 유저정보가 필요함
            return redirect('posts:index') 
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)