from django.db import models
from django.contrib.auth.models import User

class About(models.Model): 
    title = models.CharField(max_length=300)
    sub_title_1 = models.CharField(max_length=300)
    content_1 = models.TextField()
    sub_title_2 = models.CharField(max_length=300)
    content_2 = models.TextField()

    def __str__(self):
        return self.title

class Project(models.Model): 
    title = models.CharField(max_length=300)
    sub_title = models.CharField(max_length=300)
    link = models.CharField(max_length=300)
    image = models.ImageField(upload_to='apps/core/static/images/')

    def __str__(self):
        return self.title