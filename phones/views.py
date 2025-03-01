from django.shortcuts import render
from .models import Phones
from .forms import ContactForm, PhoneForm
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

def phone_create(request):
    if request.method == 'Post':
        phone = Phones()
        phone.make = request.POST.get('make', '')


def phone_create_form(request):
    form = PhoneForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('phone-list')
    return render(request, 'phones/phone_create.html', {'form': form})


def phone_update(request, pk):
    phone = Phones.objects.get(id=pk)
    if request.method == 'POST':
        phone.make = request.POST.get('make', phone.make)
        phone.model = request.POST.get('model', phone.model)
        phone.year = request.POST.get('year', phone.year)
        phone.color = request.POST.get('color', phone.color)
        phone.price = request.POST.get('price', phone.price)
        phone.description = request.POST.get('description', phone.description)
        phone.image = request.FILES.get('image', phone.image)
        phone.save()
        return redirect('phone-detail', pk=pk)
    return render(request, 'phones/phone_update.html', {'phone': phone})


from django.shortcuts import render, get_object_or_404, redirect
from .models import Phones


def phone_delete(request, pk):
    phone = get_object_or_404(Phones, id=pk)
    if request.method == 'POST':
        phone.delete()
        return redirect('phone-list')  # O'chirilgandan keyin ro'yxatga qaytadi

    return render(request, 'phones/phone_delete.html', {'phone': phone})


def contact_form(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        phone_number = form.cleaned_data['phone_number']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        print(f'Name: {name}, Phone: {phone_number}, Email: {email}, Message: {message}')
        return redirect('home')
    return render(request, 'contact.html', {'form': form})

