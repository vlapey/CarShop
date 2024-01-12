from rest_framework import serializers
from .models import DealersLoyalties, VendorsLoyalties


class DealersLoyaltiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealersLoyalties
        fields = '__all__'


class VendorsLoyaltiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorsLoyalties
        fields = '__all__'
