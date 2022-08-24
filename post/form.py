from dataclasses import fields
from operator import contains
from pyexpat import model
from socket import fromshare
from turtle import title
from .models import post
from django import forms

class formpost(forms.ModelForm):
    class Meta:
        model=post #table-name
        fields=['title','continant']
