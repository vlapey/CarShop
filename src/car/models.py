from django.db import models
from core.abstract_models import ModelProperties
from core.enums import Color, CarType, CarEngineType
from src.customer.models import Customer
from src.dealer.models import Dealer
from src.vendor.models import Vendor


class Car(ModelProperties):
    brand = models.CharField(max_length=20, default='none')
    model = models.CharField(max_length=30)
    engine = models.CharField(max_length=10, choices=CarEngineType.choices(), default='diesel')
    horsepower = models.PositiveIntegerField(default=0)
    torque = models.PositiveIntegerField(default=0)
    car_type = models.CharField(max_length=20, choices=CarType.choices(), default='sedan')

    color = models.CharField(max_length=10, choices=Color.choices(), default='black')
    mileage = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_car',
                                 null=True, default=None, blank=True)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name='dealer_car',
                               null=True, default=None, blank=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='vendor_car',
                               null=True, default=None, blank=True)
