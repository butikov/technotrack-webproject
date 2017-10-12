from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def user_page(request, user_id=None):
    return render(request, 'user_page.html', {'id': user_id})


def event_page(request, event_id=None):
    return render(request, 'event.html', {'id': event_id})


def new_event(request):
    return render(request, 'new_event.html')


def register(request):
    return render(request, 'register.html')
