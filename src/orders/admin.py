from django.contrib import admin
from .models import DealerOrder, CustomerOrder

admin.site.register(DealerOrder)
admin.site.register(CustomerOrder)
