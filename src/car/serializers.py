from rest_framework import serializers
from .models import Car


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        exclude = ('is_active', 'customer', 'dealer', 'vendor')
