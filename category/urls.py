from django.conf.urls import url
from django.views.generic import DetailView

from .models import Category
from .views import CategoryList

urlpatterns = [
    url(r'^$', CategoryList.as_view(), name='cats_list'),
    url(r'^(?P<slug>[-\w]+)/$', DetailView.as_view(model=Category, template_name='category.html',
                                                   slug_field='title'), name='cat_page'),
]
