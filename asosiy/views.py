from django.shortcuts import render,redirect
from django.views import View
from .models import *
from user.models import Sotuvchi
class Bolimlarview(View):

    def get(self,request):
        if request.user.is_authenticated:
            return render(request, 'bulimlar.html')
        return redirect('/')
class Mahsulotview(View):
    def post(self,request):
        if request.user.is_authenticated:

            Mahsulot.objects.create(
                nom=request.POST.get('nom'),
                brend=request.POST.get('brand'),
                narx=request.POST.get('narx'),
                miqdor=request.POST.get('miqdor'),
                kelgan_sana=request.POST.get('k_sana'),
                sotuvchi=Sotuvchi.objects.get(user=request.user)
            )
            return redirect('/bolimlar/mahsulotlar/')
        return redirect('/')


    def get(self, request):
        if request.user.is_authenticated:
            data={
                'mahsulotlar':Mahsulot.objects.filter(sotuvchi__user=request.user)
            }
            return render(request,'products.html',data)
        return redirect('/')
class Mijozlarview(View):
    def post(self,request):
        if request.user.is_authenticated:

            Mijoz.objects.create(
                ism=request.POST.get('client'),
                nom=request.POST.get('nom'),
                tel=request.POST.get('tel'),
                manzil=request.POST.get('manzil'),
                qarz=request.POST.get('qarz'),
                sotuvchi=Sotuvchi.objects.get(user=request.user)
            )
            return redirect('/bolimlar/mijozlar/')
        return redirect('/')
    def get(self,request):
        if request.user.is_authenticated:
            data={
                'mijozlar':Mijoz.objects.filter(sotuvchi__user=request.user)
            }
            return render(request,'clients.html', data)
        return redirect('/')
class ProductDeleteView(View):
    def get(self,request,pk):
        if request.user.is_authenticated:
            hozirgi_sotuvchi=Sotuvchi.objects.get(user=request.user)
            m=Mahsulot.objects.get(id=pk)
            if m.sotuvchi==hozirgi_sotuvchi and request.user.is_staff:
                m.delete()
            return redirect('mahsulotlar')

        return redirect('login')
class ClientDeleteView(View):
    def get(self,request,pk):
        if request.user.is_authenticated:
            a=Sotuvchi.objects.get(user=request.user)
            c=Mijoz.objects.get(id=pk)
            if c.sotuvchi==a and request.user.is_staff:
                c.delete()
            return redirect('mijozlar')
        return redirect('login')

class ClientUpdateView(View):
    def post(self,request,pk):
        Mijoz.objects.filter(id=pk).update(
            ism=request.POST.get('client'),
            nom=request.POST.get('nom'),
            tel=request.POST.get('tel'),
            manzil=request.POST.get('manzil'),
            qarz=request.POST.get('qarz'),
        )
        return redirect('/bolimlar/mijozlar/')

    def get(self,request,pk):
        if request.user.is_authenticated:

            a = Sotuvchi.objects.get(user=request.user)
            b = Mijoz.objects.get(id=pk)
            if b.sotuvchi == a and request.user.is_staff:
                data={
                    'client':b
                }
                return render(request,'client_update.html',data)
        return redirect('mijozlar')

class MahsulotUpdateView(View):
    def post(self,request,pk):

        Mahsulot.objects.filter(id=pk).update(
            nom=request.POST.get('nom'),
            brend=request.POST.get('brand'),
            narx=request.POST.get('narx'),
            miqdor=request.POST.get('miqdor'),
            olchov=request.POST.get('olchov'),
        )
        return redirect('mahsulotlar')


    def get(self, request, pk):
        hozirgi_ombor = Sotuvchi.objects.get(user=request.user)
        product = Mahsulot.objects.get(id=pk)
        if request.user.is_authenticated and hozirgi_ombor == product.sotuvchi:
            data = {
                'mahsulot':product
            }
            return render(request, 'product_update.html', data)
        else:
            return redirect('mahsulotlar')