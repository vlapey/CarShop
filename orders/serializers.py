from rest_framework import serializers
from .models import CustomerOrder, DealerOrder


class CustomerOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerOrder
        fields = '__all__'


class DealerOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealerOrder
        fields = '__all__'
