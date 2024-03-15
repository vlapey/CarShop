from rest_framework import serializers
from .models import DealersLoyalties, VendorsLoyalties


class DealersLoyaltiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealersLoyalties
        exclude = ('is_active', )


class VendorsLoyaltiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorsLoyalties
        exclude = ('is_active', )
