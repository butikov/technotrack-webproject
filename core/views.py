from cities.models import City
from dal import autocomplete
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import reverse
from django.views.generic import CreateView, DetailView, TemplateView

from event.models import Event


class CountryAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = City

        if self.q:
            qs = qs.filter(name__isstartswidth=self.q)

        return qs


class MyUserCreation(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name',
                  'avatar', 'country', 'languages',)

    def save(self, commit=True):
        user = super(MyUserCreation, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.country = self.cleaned_data["country"]
        user.languages = self.cleaned_data["languages"]
        if commit:
            user.save()
        return user


class RegistrationView(CreateView):
    form_class = MyUserCreation
    template_name = 'register.html'

    def get_success_url(self):
        return reverse('index')


class UserView(DetailView):
    model = get_user_model()
    context_object_name = 'user'
    template_name = 'user_page.html'


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['events'] = Event.objects.all()
        return context
