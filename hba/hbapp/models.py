from django.db import models

# Create your models here.
class State(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name
class City(models.Model):
    name=models.CharField(max_length=50)
    state=models.ForeignKey(State,on_delete=models.CASCADE,related_name='cities')
    def __str__(self) -> str:
        return self.name
class Hospital(models.Model):
    name=models.CharField(max_length=50)
    city=models.ForeignKey(City,on_delete=models.CASCADE,related_name='hospitals')
    phone=models.CharField(max_length=12)
    address=models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name
class Facility(models.Model):
    # hospital=models.OneToOneField(Hospital,on_delete=models.CASCADE,primary_key=True)
    # oxygen_beds_total=models.IntegerField(default=0)
    # oxygen_beds_available=models.IntegerField(default=0)
    # oxygen_cylinder_total=models.IntegerField(default=0)
    # oxygen_cylinder_available=models.IntegerField(default=0)
    # ventilator_available=models.IntegerField(default=0)
    title=models.CharField(max_length=60,null=False,blank=False,default="")
    def __str__(self) -> str:
        return self.title
class Availability(models.Model):
    hospital=models.ForeignKey(Hospital,on_delete=models.CASCADE,related_name='availabilities')
    # oxygen_beds_total=models.IntegerField(default=0)
    # oxygen_beds_available=models.IntegerField(default=0)
    # oxygen_cylinder_total=models.IntegerField(default=0)
    # oxygen_cylinder_available=models.IntegerField(default=0)
    # ventilator_available=models.IntegerField(default=0)
    facility=models.ForeignKey(Facility,on_delete=models.CASCADE,related_name='availabilities')
    updated_at=models.DateTimeField(auto_now=True)
    total=models.IntegerField(default=0)
    available=models.IntegerField(default=0)
    


    def __str__(self) -> str:
        return f"{self.hospital.name}-{self.facility.title}"



