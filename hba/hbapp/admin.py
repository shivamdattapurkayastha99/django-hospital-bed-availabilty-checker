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

    

admin.site.register(State)
admin.site.register(City)
admin.site.register(Hospital,HospitalAdmin)
admin.site.register(Facility,FacilityAdmin)


