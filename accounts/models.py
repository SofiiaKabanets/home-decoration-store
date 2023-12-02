from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.urls import reverse
import uuid 
# Create your models here.

class CustomUser(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    dob = models.DateField(null=True, blank=True,verbose_name = 'Date of Birth')
    phone = models.CharField(max_length=10, blank=True, null=True, verbose_name='Phone Number')
    signup_date = models.DateTimeField(auto_now_add=True, blank = True, null= True)

class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        null=True,
        on_delete=models.CASCADE,
    )
    fname = models.TextField(max_length=20,blank = True)
    lname = models.TextField(max_length=20,blank = True)
    biography = models.TextField(max_length=50,blank = True)
    picture = models.ImageField(upload_to='profile', blank=True)
    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse('profile_view',args=[str(self.id)])
    
    