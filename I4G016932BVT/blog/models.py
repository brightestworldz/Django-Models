from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class post(models.Model):
    author = models.ForeignKey(User, related_name='author', on_delete= models.CASCADE)
    Title  = models.CharField(max_length=200)
    Text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now_add=True)
