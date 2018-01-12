from django.conf.urls import url
from django.views.generic import DetailView

from .models import Category
from .views import CategoryAutoComplete
from .views import CategoryList

urlpatterns = [
    url(r'^$', CategoryList.as_view(), name='cats_list'),
    url(r'^category-autocomplete/$', CategoryAutoComplete.as_view(model=Category, create_field='title'),
        name='cat-autocomplete'),
    url(r'^(?P<slug>[-\w]+)/$', DetailView.as_view(model=Category, template_name='category.html',
                                                   slug_field='title'), name='cat_page'),

]
