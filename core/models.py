from django.db import models

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=255)
    creator = models.IntegerField()


class User(models.Model):
    name = models.CharField(max_length=63)
