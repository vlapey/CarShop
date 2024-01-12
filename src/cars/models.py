from django.db import models
from core.abstract_models import ModelProperties
from core.enums import Color, CarType


class CarSpecification(ModelProperties):
    name = models.CharField(max_length=30, unique=True)
    engine = models.CharField(max_length=60)
    horsepower = models.IntegerField(default=0)
    torque = models.IntegerField(default=0)

    # def __str__(self):
    #     return f'{self.name}, {self.engine}, {self.horsepower}, {self.torque}'


class Cars(ModelProperties):
    brand = models.CharField(max_length=60)
    specification = models.ForeignKey(CarSpecification, on_delete=models.CASCADE,
                                      related_name='specification_car')
    car_type = models.CharField(max_length=20, choices=CarType.choices(), default='sedan')
    color = models.CharField(max_length=10, choices=Color.choices(), default='black')

    def __str__(self):
        return self.brand
