from django.shortcuts import render
import random
# Create your views here.

def lotto(request):
    nums = [x for x in range(1, 46)]
    random_num = random.sample(nums, 6)

    context = {
        'random_num': random_num
    }
    return render(request, "lotto.html", context)
