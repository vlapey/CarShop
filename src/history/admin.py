from django.contrib import admin
from .models import CustomerDealerHistory, DealerVendorHistory

admin.site.register(CustomerDealerHistory, DealerVendorHistory)
