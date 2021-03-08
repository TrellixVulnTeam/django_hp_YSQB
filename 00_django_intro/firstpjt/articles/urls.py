from django.urls import path
# 명시적 상대 경로 표현
from . import views 

urlpatterns = [
    path('index/', views.index, name='index'),
    path('greetings/', views.greeting, name='greeting'),
    path('dinners/', views.dinner, name='dinner'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('hello/<str:name>/', views.hello, name='hello'),
]
