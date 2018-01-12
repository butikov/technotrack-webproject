from django.shortcuts import reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import NewEventForm
from .models import Event


class NewEventView(CreateView):
    template_name = 'new_event.html'
    form_class = NewEventForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(NewEventView, self).form_valid(form)

    def get_success_url(self):
        return reverse('events:event_page', kwargs={'pk': self.object.pk})


class EventUpdate(UpdateView):
    model = Event
    template_name = 'update_event.html'
    fields = 'title', 'description', 'coordinates', 'max_participants', 'event_time'

    def get_queryset(self):
        return super(EventUpdate, self).get_queryset().filter(author=self.request.user)

    def get_success_url(self):
        return reverse('events:event_page', kwargs={'pk': self.object.pk})


class EventView(DetailView):
    template_name = 'event.html'
    context_object_name = 'event'
    model = Event


class EventList(ListView):
    model = Event
    paginate_by = 20
    context_object_name = 'events'
