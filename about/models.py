from django.db import models

# Create your models here.
class about(models.Model):
    about_me=models.CharField(max_length=50)
    image=models.ImageField(upload_to='about')
    subtitle=models.CharField(max_length=500)
    tw_link=models.URLField()
    fb_link=models.URLField()
    github_link=models.URLField()


    