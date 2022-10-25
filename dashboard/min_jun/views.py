from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def min_jun(request):
    return HttpResponse("민준님의 페이지입니다!")

