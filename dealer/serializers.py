from rest_framework import serializers
from .models import Dealer, DealerCar


class DealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer
        fields = '__all__'
