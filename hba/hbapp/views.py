from django.shortcuts import render,HttpResponse
from .models import Availability, Facility, Hospital,State,City

# Create your views here.
def home(request):
    selected_state_id=request.GET.get('state')
    facilities=Facility.objects.all().order_by('pk')
    if selected_state_id:
        cities=City.objects.filter(state=selected_state_id)
    else:
        cities=City.objects.all()

    states=State.objects.all()
    hospitals=Hospital.objects.all()
    availabilities=Availability.objects.all()

    context={
        'facilities':facilities,
        'cities':cities,
        'states':states,
        'hospitals':hospitals,
        'availabilities':availabilities,
        'selected_state_id':selected_state_id
    }
    return render(request,'hbapp/index.html',context=context)
    