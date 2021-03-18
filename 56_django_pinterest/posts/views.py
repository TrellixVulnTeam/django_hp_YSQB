from django.shortcuts import render
from django.views.decorators.http import require_http_methods, require_POST, require_safe
# Create your views here.
def index(request):
    return render(request, 'posts/index.html')

@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == 'POST':
        pass
    else:
        pass
