"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from core import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^index/$', views.index),
    url(r'^users/(?P<user_id>\d+)/$', views.user_page),
    url(r'^events/(?P<event_id>\d+)/$', views.event_page),
    url(r'^register/$', views.register),
    url(r'^new_event/$', views.new_event),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      url(r'^__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
