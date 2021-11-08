from django.contrib import admin
from django.db.models.base import Model
from .models import *
from django.db.models.signals import post_save
from django.dispatch import receiver

# Register your models here.
@receiver(post_save,sender=Hospital)
def afterhospitalsave(signal, instance,**kwargs):
    service=Service(hospital=instance)
    service.save()
class ServiceAdmin(admin.ModelAdmin):
    model=Service
    list_display=['hospital','oxygen_beds_total','oxygen_beds_available','oxygen_cylinder_total','oxygen_cylinder_available','ventilator_available']

class HospitalAdmin(admin.ModelAdmin):
    model=Hospital
    list_display=['name','phone','address','city']

    

admin.site.register(State)
admin.site.register(City)
admin.site.register(Hospital,HospitalAdmin)
admin.site.register(Service,ServiceAdmin)


