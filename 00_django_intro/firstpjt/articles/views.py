from django.shortcuts import render
import random

# Create your views here.
def index(request): # 첫 번째 인자는 반드시 request
    return render(request, 'index.html') # render 함수의 첫번째 인자는 반드시 request

def greeting(request):
    foods = ['apple', 'banana', 'coconut',]

    info = {
        'name': "Woong",
    }

    context = {
        'info': info,
        'foods': foods,
    }

    return render(request, 'greeting.html', context)

def dinner(request):
    foods = ['족발', '피자', '햄버거', '초밥',]
    pick = random.choice(foods)

    context = {
        'pick': pick,
        'foods': foods,
    }
    return render(request, 'dinner.html', context)