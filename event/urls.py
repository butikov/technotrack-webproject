from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import NewEventView, EventView, EventUpdate

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', EventView.as_view(), name='event_page'),
    url(r'^new/$', login_required(NewEventView.as_view(), login_url='login'), name='new_event'),
    url(r'^(?P<pk>\d+)/update$', login_required(EventUpdate.as_view()), name='update_event')
]
