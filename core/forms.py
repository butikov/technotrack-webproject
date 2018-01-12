from dal import autocomplete
from django import forms

from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {'city': autocomplete.ModelSelect2(url='country-autocomplete')}
