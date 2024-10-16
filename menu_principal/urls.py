from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('opcoes/', views.inicio),
    path('sair/', views.sair, name='sair'),
]