from django import forms
from mapwidgets.widgets import GooglePointFieldWidget, GoogleStaticMapWidget

from .models import Event


class NewEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'description', 'event_time', 'max_participants', 'coordinates', 'categories')
        widgets = {'coordinates': GooglePointFieldWidget}


class EventDetailForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'description', 'event_time', 'participants', 'categories', 'coordinates',)
        widgets = {'coordinates': GoogleStaticMapWidget}
