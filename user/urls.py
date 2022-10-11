from django.urls import path
from .views import *


urlpatterns = [
    path('', Loginview.as_view(), name='login'),
    path('logout/', Logoutview.as_view(), name='logout'),
]