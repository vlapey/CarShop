from django.db import models
from core.abstract_models import ModelProperties
from django_countries.fields import CountryField


class Dealer(ModelProperties):
    name = models.CharField(max_length=30, unique=True)
    location = CountryField(blank_label='select country')
    balance = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def __str__(self):
        return f'{self.dealer.name} {self.car.model}'
