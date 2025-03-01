from django.urls import path
from .views import home, phone_list, phone_detail, phone_delete, phone_update, phone_create_form, phone_create, contact_form

urlpatterns = [
    path('', home, name='home'),
    path('phone_list/', phone_list, name='phone-list'),
    path('phone/<int:pk>', phone_detail, name='phone-detail'),
    path('car-create/', phone_create_form, name='phone-create'),
    path('phone-update/<int:pk>/', phone_update, name='phone-update'),
    path('phone-delete/<int:pk>/', phone_delete, name='phone-delete'),
    path('contact/', contact_form, name='contact'),
]