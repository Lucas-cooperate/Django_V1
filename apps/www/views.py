from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse


# Create your views here.

def login(request):
    result = reverse("n1")
    print(result)
    return HttpResponse("欢迎登录！！！")


def info(request, v1):
    print(v1)
    return HttpResponse(f"欢迎{v1}登录！！")


def yy(request, a1, a2, a3):
    print(a1, a2, a3)
    return HttpResponse(f"{a1}-{a2}-{a3}")


