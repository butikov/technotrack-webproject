from django.contrib import admin

from .models import Category
from .models import Event


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'title'
    list_editable = 'title',


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = 'id', 'title'
    list_editable = 'title',
    pass
