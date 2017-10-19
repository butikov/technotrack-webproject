from django.conf.urls import url

from .views import category, cat_list

urlpatterns = [
    url(r'^$', cat_list, name='cats_list'),
    url(r'^(?P<cat_name>\w+)/$', category, name='cat_page'),
]
