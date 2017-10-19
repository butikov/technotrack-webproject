from django.shortcuts import render, get_object_or_404

from .models import Event


def event_page(request, event_id=None):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'event.html', {'event': event})


def new_event(request):
    return render(request, 'new_event.html')
