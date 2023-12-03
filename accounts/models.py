import uuid 
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class CustomUser(AbstractUser):
    dob = models.DateField(null=True, blank=True,verbose_name = 'Date of Birth')
    phone = models.CharField(max_length=10, blank=True, null=True, verbose_name='Phone Number')
    signup_date = models.DateTimeField(auto_now_add=True, blank = True, null= True)

    def save(self, *args, **kwargs): # For creating a new Profile model each time a Custom User is created. 
        is_new_user = not self.pk
        super().save(*args, **kwargs)
        if is_new_user:
            Profile.objects.create(user=self)


class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        null=True,
        on_delete=models.CASCADE,
    )
    fname = models.TextField(max_length=10,blank = True)
    lname = models.TextField(max_length=10,blank = True)
    biography = models.TextField(max_length=30,blank = True)
    picture = models.ImageField(upload_to='profile', blank=True)
    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse('profile_view',args=[str(self.id)])
