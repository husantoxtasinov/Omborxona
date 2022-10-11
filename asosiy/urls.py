from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Bolimlarview.as_view(), name='bolimlar'),
    path('mahsulotlar/', Mahsulotview.as_view(), name='mahsulotlar'),
    path('mijozlar/', Mijozlarview.as_view(), name='mijozlar'),

]