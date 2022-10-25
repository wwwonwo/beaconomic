from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def ji_hun(request):
    return HttpResponse("지훈님의 페이지입니다!")

