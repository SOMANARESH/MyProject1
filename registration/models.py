from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from .choices import *

class State(models.Model):
    name = models.CharField(choices = STATE_CHOICE, max_length = 100)
    

class Location(models.Model):
    city = models.CharField(max_length = 50)
    state = models.ForeignKey(State)
    
class UserProfile(models.Model):
    user_id = models.ForeignKey(User, null=False)
    
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    #image = models.ImageField(upload_to='images/', null=True, blank=True)
    location = models.CharField(max_length=140)  
    gender = models.CharField(max_length=10, choices = GENDER)
    #profile_picture = models.ImageField(upload_to='thumbpath', blank=True, null = True)
    
    def __str__(self):
        return self.user_id.username + " -- " + self.user_id.email + " -- " + self.gender