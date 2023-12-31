"""
URL configuration for djangoProject_V1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from apps.www import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login, name='n1'),
    path('info/<int:v1>/', views.info),
    re_path(r'yy/(\d{4})-(\d{2})-(\d{2})/', views.yy),
    path('web/', include("apps.www.urls")),
    path('api/', include("apps.app01.urls")),
    path('user/', views.UserView.as_view()),
    path('demo/', views.demo),
    path('demo1/', views.demo1),
    path('order/', views.order),
    path('excel/', views.excel),
    path('my_func/', views.nb),
]
