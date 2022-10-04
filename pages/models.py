from email.mime import image
from django.db import models
#from django.contrib.auth.models import User




#class Employee(models.Model):
  # user = models.OneToOneField(User, on_delete=models.CASCADE)
  # phonenumber = models.CharField(verbose_name="phone number", max_lenght=10)
  # birthdate = models.DateField(verbose_name="birth date")

class pages(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  


class Product(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    Dept_name = models.CharField(max_length=20)
    joining_date = models.DateField(auto_now_add=True)
    Price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='None')
   
   
    


