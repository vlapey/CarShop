from django.db import models
from core.abstract_models import ModelProperties
from car.models import Car


class DealersLoyalties(ModelProperties):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    name = models.CharField(max_length=30)
    description = models.TextField(default='')
    discount = models.IntegerField(default=0)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car_promotion')
    #dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE,
    #                                  related_name='specification_car')

    def __str__(self):
        return f'{self.name} {self.car.model} {self.discount}%'


class VendorsLoyalties(ModelProperties):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    name = models.CharField(max_length=30)
    description = models.TextField(default='')
    discount = models.IntegerField(default=0)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car_promotion')
    #dealer = models.ForeignKey()
