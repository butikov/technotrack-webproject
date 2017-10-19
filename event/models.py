from datetime import datetime

from django.conf import settings
from django.db import models

from category.views import Category
from core.models import countries


class Event(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='own_events')
    title = models.CharField(max_length=255, verbose_name='Имя события')
    description = models.TextField()
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='participated_events')
    event_time = models.DateTimeField(default=datetime.now, blank=True)
    max_participants = models.IntegerField(default=-1)
    create_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    country = models.CharField(max_length=2, choices=countries, default='RU')
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    categories = models.ManyToManyField(Category, related_name='events')
    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
