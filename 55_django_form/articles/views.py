from django.shortcuts import render, redirect
from .forms import ArticleForm, ArticleModelForm
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all().order_by('-id')
    context = {
        'articles': articles,
    }

    return render(request, 'articles/index.html', context)


def new(request):
    form = ArticleForm()
    model_form = ArticleModelForm()

    # print(dir(form))

    context = {
        'form':form,
        'model_form': model_form,
    }

    return render(request, 'articles/new.html', context)


def create(request):
    # 기본 저장 구조
    # title = request.POST.get('title')
    # content = request.POST.get('content')

    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 모델 폼을 이용한 데이터 저장
    model_form = ArticleModelForm(request.POST)
    # print(model_form)
    if model_form.is_valid():
        model_form.save()

    return redirect('articles:index')

def new_create(request):
    # 5. POST 방식으로 요청 (옳은 데이터 저장해주세요)
    # 10. POST 방식으로 요청 (옳은 데이터 저장해주세요!)
    if request.method == 'POST':
        # 6. 빈 종이에 데이터 입력
        # 11. 옳은 데이터 입력
        form = ArticleModelForm(request.POST)
        # 7. 유효성 검사(실패)
        # 12. 유효성 검사(성공)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    # 1. Get 방식으로 요청(빈 종이 주세요)
    else:
        # 2. 빈 종이; 생성(모델 폼)
        form = ArticleModelForm()
    # 3. 빈종이를 사용자에게 전송
    # 8. 유효성 검사를 통과한 데이터만 입력되어 있는 종이를 전송
    context = {
        'form': form
    }
    # 4. html 파일 렌더링 (빈 종이 포함)
    # 9. html 파일 렌더링 (유효성 검사를 통과한 데이터 포함)
    return render(request, 'articles/form.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)

    context = {
        'article': article,
    }

    return render(request, 'articles/detail.html', context)


def update(request, pk):
    # 새로 입력한 데이터 저장
    article = Article.objects.get(pk=pk)    
    if request.method == 'POST':
        form = ArticleModelForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)

    else:  # GET 방식일 때
        # 기존 데이터 출력
        form = ArticleModelForm(instance=article)

        context = {
            'form': form
        }
        return render(request, 'articles/form.html', context)

def delete(request, pk):
    article = Article.objects.get()
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    
    return redirect('articles:detail', articles.pk)