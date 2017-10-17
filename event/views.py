from django.shortcuts import render, get_object_or_404

from .models import Event, Category


def event_page(request, event_id=None):
    event = get_object_or_404(Event.objects, id=event_id)
    return render(request, 'event.html', {'event': event})


def new_event(request):
    return render(request, 'new_event.html')


def cat_list(request):
    return render(request, 'cat_list.html', {'categories': Category.objects})


def category(request, cat_name):
    cat = get_object_or_404(Category.objects, title=cat_name)
    return render(request, 'category.html', {'category': cat})
