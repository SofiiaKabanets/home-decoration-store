from django.db import models
from django.urls import reverse
from accounts.models import Profile

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 200)
    body = models.TextField()
    
    
    def __str__(self):
        return self.id
    
    
    def get_absolute_url(self):
        return reverse("review_detail", args = [str(self.id)])
    