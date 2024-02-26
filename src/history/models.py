from django.db import models
from core.abstract_models import ModelProperties
from src.dealer.models import Dealer
from src.customer.models import Customer
from src.vendor.models import Vendor
from src.loyalties.models import VendorsLoyalties, DealersLoyalties
from src.car.models import Car


class History(ModelProperties):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True


class CustomerDealerHistory(History):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_dealer_history')
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name='dealer_customer_history')
    discount = models.ForeignKey(DealersLoyalties, on_delete=models.CASCADE)

    def __str__(self):
        return f"customer {self.customer.name} dealer {self.dealer.name}"


class DealerVendorHistory(History):
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name='dealer_vendor_history')
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='vendor_dealer_history')
    discount = models.ForeignKey(VendorsLoyalties, on_delete=models.CASCADE)

    def __str__(self):
        return f"dealer {self.dealer.name} vendor {self.vendor.name}"
