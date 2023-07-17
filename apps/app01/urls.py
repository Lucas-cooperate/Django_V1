from django.urls import path
from apps.app01 import views

urlpatterns = [
    path('user/', views.user)
]