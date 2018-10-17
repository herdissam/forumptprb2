from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def tentang(request):
    return render(request, 'tentang.html')

def jawatimur(request):
    return render(request, 'jawatimur.html')


