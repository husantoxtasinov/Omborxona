from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Bolimlarview.as_view(), name='bolimlar'),
    path('mahsulotlar/', Mahsulotview.as_view(), name='mahsulotlar'),
    path('mijozlar/', Mijozlarview.as_view(), name='mijozlar'),
    path('pr_delete/<int:pk>/',ProductDeleteView.as_view(), name='pr_delete'),
    path('pr_delete/<int:pk>/',ClientDeleteView.as_view(), name='pr_delete'),
    path('cl_update/<int:pk>/',ClientUpdateView.as_view(), name='cl_update'),
    path('pr_update/<int:pk>/',MahsulotUpdateView.as_view(), name='pr_update'),

]