from django.db import models
from core.abstract_models import ModelProperties


class CarSpecification(ModelProperties):
    name = models.CharField(max_length=30, unique=True)
    engine = models.CharField(max_length=60)
    horsepower = models.PositiveIntegerField(default=0)
    torque = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Car(ModelProperties):
    model = models.CharField(max_length=60)
    specification = models.ForeignKey(CarSpecification, on_delete=models.CASCADE,
                                      related_name='specification_car')

    def __str__(self):
        return self.model
