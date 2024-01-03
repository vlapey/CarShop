from django.db import models
from core.abstract_models import ModelProperties
from src.cars.models import Car


class Loyalties(ModelProperties):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    name = models.CharField(max_length=30)
    description = models.TextField(default='')
    discount = models.IntegerField(default=0)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car_promotion')

    def __str__(self):
        return f'{self.name} {self.car.model} {self.discount}%'
