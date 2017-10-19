from django.conf.urls import url

from .views import event_page, new_event

urlpatterns = [
    url(r'^(?P<event_id>\d+)/$', event_page, name='event_page'),
    url(r'^new/$', new_event, name='new_event'),
]
