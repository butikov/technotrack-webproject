from dal import autocomplete
from django.views.generic import ListView, DetailView

from .forms import CategoriesListForm
from .models import Category


class CategoryAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Category.objects.none()
        qs = Category.objects.all()
        if self.q:
            qs = qs.filter(title__istartswith=self.q)
        return qs


class CategoryList(ListView):
    template_name = 'cat_list.html'
    context_object_name = 'categories'
    model = Category

    def get_queryset(self):
        q = super(CategoryList, self).get_queryset()
        self.form = CategoriesListForm(self.request.GET)
        if self.form.is_valid():
            if self.form.cleaned_data['order_by']:
                q = q.order_by(self.form.cleaned_data['order_by'])
            if self.form.cleaned_data['search']:
                q = q.filter(title=self.form.cleaned_data['search'])
            return q

    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(CategoryList, self).get_context_data(**kwargs)
        context['searchform'] = self.form
        return context


class CategoryDetail(DetailView):
    template_name = 'category.html'
    context_object_name = 'category'
    model = Category
    slug_field = 'title'
    query_pk_and_slug = True
