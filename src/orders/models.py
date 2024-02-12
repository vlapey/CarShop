from django.db import models
from core.abstract_models import ModelProperties
from src.car.models import Car
from src.customer.models import Customer
from src.dealer.models import Dealer


class CustomerOrder(ModelProperties):
    price = models.PositiveIntegerField(null=False)
    amount = models.PositiveIntegerField(default=1)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_customer_order')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car_customer_order')

    def __str__(self):
        return f'customer {self.customer} car {self.car.model}'


class DealerOrder(ModelProperties):
    price = models.PositiveIntegerField(null=False)
    amount = models.PositiveIntegerField(default=1)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name='dealer_dealer_order')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car_dealer_order')

    def __str__(self):
        return f'dealer {self.dealer.name} car {self.car.model}'
