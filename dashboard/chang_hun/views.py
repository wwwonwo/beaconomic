from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def chang_hun(request):
    return HttpResponse("창훈님의 페이지입니다!")

