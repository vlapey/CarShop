from django.db import models
from core.abstract_models import ModelProperties
from core.enums import Color, CarType
from src.customer.models import Customer
from src.dealer.models import Dealer
from src.vendor.models import Vendor


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
    price = models.PositiveIntegerField(default=0)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_car',
                                 null=True, default=None, blank=True)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name='dealer_car',
                               null=True, default=None, blank=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='vendor_car',
                               null=True, default=None, blank=True)
