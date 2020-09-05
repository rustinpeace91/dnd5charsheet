from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField(blank=True)
    image = models.ImageField(upload_to='media/images', default='media/images/knight.jpg')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')
