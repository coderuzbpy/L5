from django.urls import path
from .views import home, cars_list, car_detail

urlpatterns = [
    path('', home, name='home'),
    path('cars-list', cars_list, name='cars-list'),
    path('car/<int:pk>', car_detail, name='car-detail'),
]