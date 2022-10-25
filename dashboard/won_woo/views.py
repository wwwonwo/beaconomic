from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def won_woo(request):
    return HttpResponse("원우님의 페이지입니다!")

