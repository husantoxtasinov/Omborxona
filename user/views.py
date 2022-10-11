from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from django.views import View





class Loginview(View):
    def get(self,request):
        return render(request, 'home.html')
    def post(self,request):
        user=authenticate(username=request.POST.get('l'),
                          password=request.POST.get('p'))
        if user is None:
            return redirect('/')
        login(request, user)
        return redirect('/bolimlar/')

class Logoutview(View):
    def get(self,request):
        logout(request)
        return redirect('/')