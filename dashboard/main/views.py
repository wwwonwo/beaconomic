from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'main/index.html')

def chang_hun(request):
    return render(request,'main/chang_hun.html')

def ji_hun(request):
    return render(request,'main/ji_hun.html')

def jun_young(request):
    return render(request,'main/jun_young.html')

def min_jun(request):
    return render(request,'main/min_jun.html')

def won_woo(request):
    return render(request,'main/won_woo.html')