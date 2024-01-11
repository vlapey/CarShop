from django.db import models
from core.abstract_models import ModelProperties
from src.cars.models import Cars
from src.dealer.models import Dealer
from src.vendor.models import Vendor
from django.core.validators import MaxValueValidator, MinValueValidator


class DealersLoyalties(ModelProperties):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    name = models.CharField(max_length=30)
    description = models.TextField(default='')
    discount = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    car = models.ForeignKey(Cars, on_delete=models.CASCADE, related_name='car_promotion')
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE,
                               related_name='dealer_loyalties')

    def __str__(self):
        return f'{self.name} {self.car.model} {self.discount}%'


class VendorsLoyalties(ModelProperties):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    name = models.CharField(max_length=30)
    description = models.TextField(default='')
    discount = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    car = models.ForeignKey(Cars, on_delete=models.CASCADE, related_name='car_loyalties')
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE,
                               related_name='vendor_loyalties')

    def __str__(self):
        return f'{self.name} {self.car.model} {self.discount}%'
