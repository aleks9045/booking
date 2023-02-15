from django.shortcuts import render
from .forms import RegistrationForm, BookingForm

def index(request):
    return render(request, 'main/index.html')

def krasnodar(request):
    return render(request, 'main/krasnodar.html')

def sochi(request):
    return render(request, 'main/sochi.html')

def rostov_on_don(request):
    return render(request, 'main/rostov_on_don.html')

def yakutsk(request):
    return render(request, 'main/yakutsk.html')

def moscow(request):
    return render(request, 'main/moscow.html')

def saintpetersburg(request):
    return render(request, 'main/saintpetersburg.html')

def yalta(request):
    return render(request, 'main/yalta.html')

def krim(request):
    return render(request, 'main/krim.html')

def ekaterinburg(request):
    return render(request, 'main/ekaterinburg.html')


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()

    form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'main/registration.html', context)

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()

    form = BookingForm()
    context = {
        'form': form
    }
    return render(request, 'main/booking.html', context)