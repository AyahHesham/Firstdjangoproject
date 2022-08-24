from distutils.command import upload
from statistics import mode
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class post(models.Model):
    auther=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_post')
    title=models.CharField(max_length=100)
    continant=models.CharField(max_length=200)
    image=models.ImageField(upload_to='post')
    def __str__(self):
        return self.title


    

    
