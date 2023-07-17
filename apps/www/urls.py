from django.urls import path
from apps.www import views

urlpatterns = [
    path('index/', views.index, name="v2")
]