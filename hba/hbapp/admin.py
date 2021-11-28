from django.contrib import admin
from django.db.models.base import Model
from .models import *
from django.db.models.signals import post_save
from django.dispatch import receiver

# Register your models here.
@receiver(post_save,sender=Hospital)
def afterhospitalsave(signal, instance,**kwargs):
    pass
class FacilityAdmin(admin.ModelAdmin):
    model=Facility
    list_display=['title']

class HospitalAdmin(admin.ModelAdmin):
    model=Hospital
    list_display=['name','phone','address','city']
class CityAdmin(admin.ModelAdmin):
    model=City
    list_display=['name','state']
class AvailabilityAdmin(admin.ModelAdmin):
    model=Availability
    list_display=['hospital','facility','total','available','updated_at']

admin.site.register(State)
admin.site.register(City,CityAdmin)
admin.site.register(Hospital,HospitalAdmin)
admin.site.register(Facility,FacilityAdmin)
admin.site.register(Availability,AvailabilityAdmin)


