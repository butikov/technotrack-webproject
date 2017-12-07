from django.contrib import admin
from django.contrib.gis.db import models
from mapwidgets.widgets import GooglePointFieldWidget

from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = 'id', 'title'
    list_editable = 'title',
    formfield_overrides = {models.PointField: {"widget": GooglePointFieldWidget}}
