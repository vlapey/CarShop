from django.db import models
from core.abstract_models import ModelProperties
from dealer.models import Dealer
from customer.models import Customer
from vendor.models import Vendor


class CustomerDealerHistory(ModelProperties):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_dealer_history')
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name='dealer_customer_history')

    def __str__(self):
        return f"customer {self.customer.name} dealer {self.dealer.name}"


class DealerVendorHistory(ModelProperties):
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name='dealer_vendor_history')
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='vendor_dealer_history')

    def __str__(self):
        return f"dealer {self.dealer.name} vendor {self.vendor.name}"
