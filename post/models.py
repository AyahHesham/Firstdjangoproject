from distutils.command import upload
from statistics import mode
from django.db import models


# Create your models here.
class post(models.Model):
    title=models.CharField(max_length=100)
    continant=models.CharField(max_length=200)
    image=models.ImageField(upload_to='post')
    def __str__(self):
        return self.title


    

    
