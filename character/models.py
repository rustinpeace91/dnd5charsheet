from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Character(models.Model):
    name = models.CharField(max_length=100, unique=True)
    char_class = models.CharField(max_length=50)
    level = models.IntegerField()
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='media/images', default='media/images/knight.jpg')


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')
