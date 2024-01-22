from django.db import models
from core.abstract_models import ModelProperties
from core.enums import Color, CarType


class CarSpecification(ModelProperties):
    brand = models.CharField(max_length=20, default='none')
    model = models.CharField(max_length=30, unique=True)
    engine = models.CharField(max_length=60)
    horsepower = models.PositiveIntegerField(default=0)
    torque = models.PositiveIntegerField(default=0)
    car_type = models.CharField(max_length=20, choices=CarType.choices(), default='sedan')


class Cars(ModelProperties):

    specification = models.ForeignKey(CarSpecification, on_delete=models.CASCADE,
                                      related_name='specification_car')

    color = models.CharField(max_length=10, choices=Color.choices(), default='black')
    mileage = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.mileage
