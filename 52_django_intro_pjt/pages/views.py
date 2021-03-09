import requests
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')


def dtl(request):
    foods = ['라면', '짜장면', '떡볶이']
    user_info = {
        'name': 'woong',
        'location': 'seoul',
    }
    nums = [500, 4]

    context = {
        'foods': foods,
        'user_info': user_info,
        'nums': nums,
    }

    return render(request, 'pages/dtl.html', context)

def question(request):
    return render(request, 'pages/question.html')


def answer(request):
    user_q = request.GET.get('q')
    url = 'https://yesno.wtf/api'
    res = requests.get(url)
    # print(res.json())
    yesorno = res.json()

    context = {
        'yesorno': yesorno,
        'user_q': user_q
    }

    return render(request, 'pages/answer.html', context)

