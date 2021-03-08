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