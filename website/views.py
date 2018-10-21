from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def tentang(request):
    return render(request, 'tentang.html')

def jawatimur(request):
    return render(request, 'jawatimur.html')

def article1(request):
    return render(request, 'article1.html')

def article2(request):
    return render(request, 'article2.html')

def article3(request):
    return render(request, 'article3.html')

def article4(request):
    return render(request, 'article4.html')

def article5(request):
    return render(request, 'article5.html')

def article6(request):
    return render(request, 'article6.html')
# def article(request):
#    queryset  = Post.objects.all()
#    context = {
#        "object_list": queryset
#    }


