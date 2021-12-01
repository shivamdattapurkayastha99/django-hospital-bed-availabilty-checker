from django.shortcuts import render,HttpResponse
from .models import Availability, Facility, Hospital,State,City

# Create your views here.
def home(request):
    facilities=Facility.objects.all().order_by('title')
    cities=City.objects.all()
    states=State.objects.all()
    hospitals=Hospital.objects.all()
    availabilities=Availability.objects.all()

    context={
        'facilities':facilities,
        'cities':cities,
        'states':states,
        'hospitals':hospitals,
        'availabilities':availabilities
    }
    return render(request,'hbapp/index.html',context=context)
    