from django.shortcuts import render,HttpResponse
from .models import Availability, Facility, Hospital,State,City
from django.views import generic
# Create your views here.

class HospitalDetailView(generic.DetailView):
    model=Hospital

def home(request):
    selected_state_id=request.GET.get('state')
    selected_city_id=request.GET.get('city')
    selected_facility_id=request.GET.get('facility')
    facilities=Facility.objects.all().order_by('pk')
    hospitals=Hospital.objects.all()
    if selected_state_id:
        cities=City.objects.filter(state=selected_state_id)
    else:
        cities=City.objects.all()
    if selected_city_id:
        hospitals=hospitals.filter(city=City(pk=selected_city_id))
    if selected_facility_id:
        availabilities=Availability.objects.all()
        if selected_city_id:
            availabilities=availabilities.filter(city=City(pk=selected_city_id))
        availabilities=availabilities.filter(facility=Facility(pk=selected_facility_id),available__gt=0)

        
        hospitals=[]
        for avl in availabilities:

            hospitals.append(avl.hospital)



    states=State.objects.all()
    
    availabilities=Availability.objects.all()

    context={
        'facilities':facilities,
        'cities':cities,
        'states':states,
        'hospitals':hospitals,
        'availabilities':availabilities,
        'selected_state_id':selected_state_id,
        'selected_city_id':selected_city_id,
        'selected_facility_id':selected_facility_id
    }
    return render(request,'hbapp/index.html',context=context)
    