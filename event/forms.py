from dal import autocomplete
from django import forms
from mapwidgets.widgets import GooglePointFieldWidget, GoogleStaticMapWidget

from .models import Event


class NewEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'description', 'event_time', 'max_participants', 'categories', 'coordinates')
        widgets = {'coordinates': GooglePointFieldWidget,
                   'categories': autocomplete.ModelSelect2Multiple(url='cats:cat-autocomplete'),
                   }


class EventDetailForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'description', 'event_time', 'participants', 'categories', 'coordinates',)
        widgets = {'coordinates': GoogleStaticMapWidget(zoom=12, size='240x240')}
