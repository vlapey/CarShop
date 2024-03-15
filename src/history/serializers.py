from rest_framework import serializers
from .models import CustomerDealerHistory, DealerVendorHistory


class CustomerDealerHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDealerHistory
        exclude = ('is_active', )


class DealerVendorHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DealerVendorHistory
        exclude = ('is_active', )
