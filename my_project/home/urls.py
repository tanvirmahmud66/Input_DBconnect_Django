from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_index),
    path('another/', views.home_another),
]