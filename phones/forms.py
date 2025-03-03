from django import forms
from pyexpat.errors import messages

from .models import Phones


class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phones
        fields = '__all__'


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)
    message = forms.CharField(widget=forms.Textarea)

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError("Ismingizni togri kiriting")
        return name
    #
    # def clean_message(self):
    #     message = self.cleaned_data['message']

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Phones
        fields = '__all__'

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price and price > 20000:
            raise forms.ValidationError("siz telefon narxini juda baland qo`ydingiz")
        return price


class PhoneDeleteForm(forms.Form):
    confirm = forms.BooleanField(
        required=True,
        label="Tasdiqlash",
        help_text="Telefonni o‘chirishni tasdiqlang"
    )





