from datetime import datetime

from django.conf import settings
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

from category.views import Category

POINT = Point(0, 0, srid=4326)


class Event(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='own_events')
    title = models.CharField(max_length=255, verbose_name='Имя события')
    description = models.TextField()
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='participated_events')
    event_time = models.DateTimeField(default=datetime.now, blank=True)
    max_participants = models.IntegerField(default=-1)
    create_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
#    coordinates = models.PointField()
    categories = models.ManyToManyField(Category, related_name='events')
    is_deleted = models.BooleanField(default=False)
