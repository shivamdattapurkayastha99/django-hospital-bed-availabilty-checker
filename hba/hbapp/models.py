from django.db import models

# Create your models here.
class State(models.Model):
    name=models.CharField(max_length=50)
class City(models.Model):
    name=models.CharField(max_length=50)
    state=models.ForeignKey(State,on_delete=models.CASCADE,related_name='cities')
class Hospital(models.Model):
    name=models.CharField(max_length=50)
    city=models.ForeignKey(City,on_delete=models.CASCADE,related_name='hospitals')
    phone=models.CharField(max_length=12)
    address=models.CharField(max_length=200)
class Service(models.Model):
    hospital=models.OneToOneField(Hospital,on_delete=models.CASCADE,primary_key=True)
    oxygen_beds_total=models.IntegerField(default=0)
    oxygen_beds_available=models.IntegerField(default=0)
    oxygen_cylinder_total=models.IntegerField(default=0)
    oxygen_cylinder_available=models.IntegerField(default=0)
    ventilator_available=models.IntegerField(default=0)
    



