from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


# Create your models here.

class User(AbstractBaseUser):
    email =models.EmailField(max_length=255)
    username=models.CharField(max_length=255)

class Product(models.Model):
    name=  models.CharField(max_length=255)
    price= models.FloatField()
    quantity= models.IntegerField()
    image= models.CharField()