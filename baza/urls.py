from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',include('user.urls')),
    path('bolimlar/',include('asosiy.urls')),
    path('stats/',include('stats.urls')),
]