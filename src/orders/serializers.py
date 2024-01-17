from rest_framework import serializers
from .models import CustomerOrder, DealerOrder


class CustomerOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerOrder
        exclude = ('is_active', )


class DealerOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealerOrder
        exclude = ('is_active', )
