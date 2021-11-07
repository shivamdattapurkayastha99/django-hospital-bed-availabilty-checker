from django.contrib import admin
from .models import *
from django.db.models.signals import post_save
from django.dispatch import receiver

# Register your models here.
@receiver(post_save,sender=Hospital)
def afterhospitalsave(signal, instance,**kwargs):
    service=Service(hospital=instance)
    service.save()
    

    

admin.site.register(State)
admin.site.register(City)
admin.site.register(Hospital)
admin.site.register(Service)


