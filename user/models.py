from django.db import models
from .constants import GENDER,BLOOD_GROUP
from . import functions


# Create your models here.
class Division(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class District(models.Model):
    name=models.CharField(max_length=50)
    division=models.ForeignKey(Division,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    

class UserModel(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    gender=models.CharField(max_length=30,choices=GENDER)
    birth_date=models.DateField()
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=50)
    blood_group=models.CharField(max_length=50,choices=BLOOD_GROUP)
    image=models.ImageField(upload_to='images/user/', default='images/male_avatar.jpg')
    division=models.ForeignKey(Division,on_delete=models.CASCADE)
    District=models.ForeignKey(District,on_delete=models.CASCADE)
    last_donate=models.DateField(auto_now_add=False, null=True, blank=True)
    availabilities=models.BooleanField(default=True)
    
    
        
    def __str__(self):
        return self.first_name + ' ' + self.last_name