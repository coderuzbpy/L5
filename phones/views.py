from django.shortcuts import render
from .models import Phones
# Create your views here.

def  home(request):
    return render(request, 'home.html')

def phone_list(request):
    phones = Phones.objects.all()
    context = {'phones': phones}
    return render(request, 'phones/smartphone_list.html', context=context)

def phone_detail(request, pk):
    phone = Phones.objects.get(id=pk)
    context = {'phone': phone}
    return render(request, 'phones/smartphone_detail.html', context=context)