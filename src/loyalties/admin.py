from django.contrib import admin
from .models import DealersLoyalties, VendorsLoyalties

admin.site.register(DealersLoyalties, VendorsLoyalties)
