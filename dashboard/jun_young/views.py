from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def jun_young(request):
    return HttpResponse("준영님의 페이지입니다!")

