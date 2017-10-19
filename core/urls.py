from django.conf.urls import url

from .views import user_page, register

urlpatterns = [
    url(r'^(?P<user_id>\d+)/$', user_page, name='user_page'),
    url(r'^new/$', register),
]
