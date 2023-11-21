from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    dob = models.DateField(null=True, blank=True,verbose_name = 'Date of Birth')
    phone = models.CharField(max_length=10, blank=True, null=True, verbose_name='Phone Number')
