from django.shortcuts import render, get_object_or_404

from event.models import Event
from .models import User


def index(request):
    return render(request, 'index.html', {'events': Event.objects.all})


def user_page(request, user_id=None):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'user_page.html', {'user': user})


def register(request):
    return render(request, 'register.html')
