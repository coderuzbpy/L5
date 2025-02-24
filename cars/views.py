from django.shortcuts import render
from .models import Cars
# Create your views here.

def home(request):
    return render(request, 'home.html')

def cars_list(request):
    cars = Cars.objects.all()
    context = {'cars': cars}
    return render(request, 'cars/cars_list.html', context=context)

def car_detail(request, pk):
    car = Cars.objects.get(id=pk)
    context = {'car': car}
    return render(request, 'cars/car_detail.html', context=context)