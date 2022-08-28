from distutils.command.upload import upload
from email import contentmanager
from email.mime import image
from pyexpat import model
from turtle import title
from django.db import models
from django.utils import timezone

# Create your models here.
class blog(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to='blog')
    content=models.TextField(max_length=1000)
    #used timezone from django to spead the opration because we now in django
    puplishdate=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title