from django.db import models
from core.abstract_models import ModelProperties
from django_countries.fields import CountryField
from src.cars.models import Cars


class Dealer(ModelProperties):
    name = models.CharField(max_length=30, unique=True)
    location = CountryField(blank_label='select country')
    balance = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class DealersCar(ModelProperties):
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name='dealer_dealer_car')
    car = models.ForeignKey(Cars, on_delete=models.CASCADE, related_name='car_dealer_car')
    amount = models.IntegerField(default=0)
    price = models.FloatField(default=.0)

    def __str__(self):
        return f'{self.dealer.name} {self.car.model}'
