from django.conf import settings
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Event(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='own_events')
    title = models.CharField(max_length=255, verbose_name='Имя события')
    description = models.TextField(default='')
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='participated_events')
    max_participants = models.IntegerField(default=-1)
    create_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    location = models.TextField()
    categories = models.ManyToManyField(Category, related_name='events')
    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
