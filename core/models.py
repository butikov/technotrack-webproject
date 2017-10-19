import pycountry
from django.contrib.auth.models import AbstractUser
from django.db import models
from multiselectfield import MultiSelectField

countries = tuple((c.alpha_2, c.name) for c in pycountry.countries)
lang_list = tuple((l.alpha_3, l.name) for l in pycountry.languages)


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    languages = MultiSelectField(max_length=39, choices=lang_list, default='rus')
    country = models.CharField(max_length=2, choices=countries, default='RU')
