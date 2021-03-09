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

import random
# Create your views here.

def lotto(request):
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=953'
    res = requests.get(url)
    lotto_info = res.json()
    
    winner = []
    for i in range(1, 7):
        winner.append(lotto_info[f"drwtNo{i}"])

    nums = [x for x in range(1, 46)]
    pick_numbers = random.sample(nums, 6)

    
    result = len(set(pick_numbers) & set(winner))

    context = {
        'pick_numbers': pick_numbers,
        'winner': winner,
        'result': result,
    }

    

    return render(request, "pages/lotto.html", context)


def dinner(request, menu, number):
    context = {
        'menu': menu,
        'number': number,
    }

    return render(request, 'pages/dinner.html', context)
