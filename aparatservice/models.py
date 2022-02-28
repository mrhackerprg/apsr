from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.

class Interface(models.Model):
    channel_name = models.CharField(max_length = 60 , blank = False , null = False)
    username = models.CharField(max_length = 60 , blank = False , null = False)
    channel_password = models.CharField(max_length = 120 , blank = False , null = False)
    phone_number = models.IntegerField(blank = False , null = False)
    email = models.EmailField(blank = False , null = False)
    followers = models.IntegerField()

class Ads(models.Model):
    title = models.CharField(max_length = 60)
    body = models.TextField()
    date_expire = models.DateField()
    who_publish = models.CharField(max_length = 60)