from django.contrib.auth.models import AbstractUser
from django.db import models

from event.models import Event


class City(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Language(models.Model):
    title = models.CharField(max_length=255)


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
