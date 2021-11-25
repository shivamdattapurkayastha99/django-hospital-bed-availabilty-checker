from django.shortcuts import render,HttpResponse
from .models import Service,State,City

# Create your views here.
def home(request):
    services=Service.objects.all()
    cities=City.objects.all()
    states=State.objects.all()

    context={
        'services':services,
        'cities':cities,
        'states':states
    }
    return render(request,'hbapp/index.html',context=context)
    