from rest_framework import serializers
from .models import CustomerDealerHistory, DealerVendorHistory


class CustomerDealerHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDealerHistory
        fields = '__all__'


class DealerVendorHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DealerVendorHistory
        fields = '__all__'
