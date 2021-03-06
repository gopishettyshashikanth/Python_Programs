from django.db import models
from django import forms
from django.core.validators import RegexValidator
from django.utils.timezone import now as timezone_now

from django.contrib.auth.models import AbstractUser

import random
import string
import os

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

STATE_CHOICES = (
    ('Telangana', 'TG'),
    ('Andhra Pradesh', 'AP'),
    ('Madhra Pradesh', 'MP')
)
ALLOW_NUMBER_ONLY = RegexValidator(r'^[0-9]*$',
                                   'Only numeric characters are allowed.')


class Dept(models.Model):
    deptName = models.CharField(max_length=20)

    def __str__(self):
        return "%s"%self.deptName
class UserCategory(models.Model):
    name = models.CharField(max_length=20)
    Email = models.CharField(max_length=20)
    salary = models.IntegerField()
    tds = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=10,
                                     validators=[ALLOW_NUMBER_ONLY],
                                     unique=True)
    #created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    gender = models.CharField(max_length=10,
                              choices=GENDER_CHOICES)
    state = models.CharField(max_length=50,
                              choices=STATE_CHOICES)
    photoID = models.ImageField(upload_to = 'images_upload')

    deptID = models.ForeignKey(Dept,blank=True, null=True)

    def __str__(self):
    	return "%s"%self.name

class User(AbstractUser):

    location = models.CharField(max_length=30)
    
    def __str__(self):
        return "%s"%self.location