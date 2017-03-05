from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import GuessNumbers
from .form import PostForm

def index(request):
    #return HttpResponse("<h1>Hello, My name is Kihoon")
    lottos = GuessNumbers.objects.all()

    # template만 연결되어 있다                         key     content
    return render(request, "lotto/default.html", {"lottos": lottos})

def post(request):
    if request.method == "POST":
        # save data
        #return HttpResponse("Post Method")
        form = PostForm(request.POST)
        if form.is_valid():
            # 로또 번호는 가져오지만 실제 디비에 저장은 안됌
            lotto = form.save(commit=False)
            lotto.generate()
            #return HttpResponse("Saved OK")
            # 메인 페이지로 리다이렉트 해주기
            return redirect('index')
    else:
        form = PostForm()
        return render(request, 'lotto/form.html', {"form":form})

def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk=lottokey)
    return render(request, "lotto/detail.html", {"lotto": lotto})