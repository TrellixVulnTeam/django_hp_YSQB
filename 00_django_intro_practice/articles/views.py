from django.shortcuts import render

# Create your views here.

def index(request):
    # print(render(request, 'index.html'))
    lunch = ['햄버고',
    '탕수육',
    '짬뽕'
    ]

    context = {
        'lunch': lunch
    }
    return render(request, "index.html", context)


def ping(request):
    return render(request, 'ping.html')

def pong(request):
    # print(dir(request))
    print(dir(request)) # request 안에 데이터
    user_id = request.GET.get('id')
    user_pw = request.GET.get('pw')
    # 회원 가입, 로그인 했다고 가정 
    context = {
        'user_id': user_id,
    } 
    return render(request, 'pong.html', context)


def detail(request, number):

    articles = [
        '게시물1',
        '게시물2',
        '게시물3',
    ]

    result = articles[number - 1]

    context = {
        'result': result
    }

    return render(request, 'detail.html', context)