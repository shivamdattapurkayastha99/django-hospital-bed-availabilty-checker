from django.shortcuts import render,HttpResponse
from .models import Facility,State,City

# Create your views here.
def home(request):
    facilities=Facility.objects.all()
    cities=City.objects.all()
    states=State.objects.all()

    context={
        'facilities':facilities,
        'cities':cities,
        'states':states
    }
    return render(request,'hbapp/index.html',context=context)
    