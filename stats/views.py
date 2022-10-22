from django.shortcuts import render,redirect
from django.views import View
from .models import *
from user.models import Sotuvchi

from asosiy.models import Mahsulot,Mijoz


class StatistikaView(View):
    def get (self,request):
        statistikalar=Statistika.objects.filter(sotuvchi__user=request.user)
        qidiruv_sozi=request.GET.get('soz')
        if qidiruv_sozi is not None :
            statistikalar = statistikalar.filter(mahsulot__nom__contains=
            qidiruv_sozi)|statistikalar.filter(mahsulot__brend__contains=
            qidiruv_sozi)|statistikalar.filter(mijoz__ism__contains=qidiruv_sozi)
        data={
            'stats':statistikalar,
            'mahsulotlar':Mahsulot.objects.all(),
            'mijozlar':Mijoz.objects.all(),
            'sotuvchilar':Sotuvchi.objects.all(),

        }
        return render(request,'stats.html',data)

    def post(self,request):
        if request.user.is_authenticated:
            Statistika.objects.create(
                mahsulot=Mahsulot.objects.get(id=request.POST.get('mahsulot')),
                mijoz=Mijoz.objects.get(id=request.POST.get('mijoz')),
                miqdor=request.POST.get('miqdor'),
                sana=request.POST.get('sana'),
                sotuvchi=Sotuvchi.objects.get(id=request.POST.get('sotuvchi')),
                jami=request.POST.get('summa'),
                tolandi=request.POST.get('tolandi'),
                nasiya=request.POST.get('nasiya'),
            )
            return redirect('/stats/stats/')
        return redirect('/')

