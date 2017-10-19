from django.conf import settings
from django.db import models

from event.models import Event


class AbstractComment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments')
    text = models.TextField()

    class Meta:
        abstract = True


class Comment(AbstractComment):
    subject = models.ForeignKey(Event, related_name='comments')


class Review(AbstractComment):
    rating = models.SmallIntegerField()
    subject = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reviews')
