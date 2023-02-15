from .models import Registration, Booking
from django.forms import ModelForm, TextInput, Textarea, ChoiceField, CheckboxSelectMultiple

class RegistrationForm(ModelForm):
    class Meta:
        model = Registration
        fields = ["name", "city", "description"]
        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Введите название отеля',
                'style': 'border-radius:8px;  width:300px;',
                'class': 'text-center'
            }),
            'city': TextInput(attrs={
                'placeholder': 'Введите название города',
                'style': 'border-radius:8px; width:300px;',
                'class': 'text-center'
            }),
            'description': Textarea(attrs={
                'placeholder': 'Введите описание',
                'style': 'border-radius:8px;',
                'class': 'text-center'
            })
        }

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['hotel', 'surname', 'name',
                  'lastname', 'number']
        widgets = {
            'hotel': TextInput(attrs={
                'placeholder': 'Введите название отеля',
                'style': 'border-radius:8px;  width:300px;',
                'class': 'text-center'
            }),
            'surname': TextInput(attrs={
                'placeholder': 'Введите фамилию',
                'style': 'border-radius:8px;  width:300px;',
                'class': 'text-center'
            }),
            'name': TextInput(attrs={
                'placeholder': 'Введите имя',
                'style': 'border-radius:8px;  width:300px;',
                'class': 'text-center'
            }),
            'lastname': TextInput(attrs={
                'placeholder': 'Введите отчество',
                'style': 'border-radius:8px;  width:300px;',
                'class': 'text-center'
            }),
            'number': TextInput(attrs={
                'placeholder': 'Введите номер',
                'style': 'border-radius:8px;  width:300px;',
                'class': 'text-center'
            })
        }