from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('stats/', StatistikaView.as_view(), name='stats'),
]