import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views import View


# Create your views here.
class UserView(View):
    # 根据请求方式触发不同请求！
    def get(self, request):
        return redirect("https://www.baidu.com")

    def post(self, request):
        return HttpResponse("User POST!!")

    def put(self, request):
        return HttpResponse("User PUT!!")

    def delete(self, request):
        return HttpResponse("User DELETE!!")


def demo(request):
    user_list = ["王坤", "李晶"]
    return render(request, "www/demo.html", {"v1": user_list})


def nb(request):
    return render(
        request,
        "www/nb.html",
        {
            'num': [11, 22, 33, 44],
            'name': "张卡",
            'ctime': datetime.datetime.now()
        }
    )


def demo1(request):
    t = "hello world!!"
    title = "测试"
    return render(request, "www/使用模板1.html", {'title': title, "t": t})


def order(request):
    title = "订单"
    return render(request, "www/使用模板2.html", {'title': title})


def excel(request):
    title = "表单"
    return render(request, "www/使用模板3.html", {'title': title})


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


def index(request):
    return HttpResponse('INDEX')