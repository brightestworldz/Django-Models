from django.db import models

# Create your models here.

class post(models.Model):
    Title  = models.CharField(max_length=200)
    Text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now_add=True)
    