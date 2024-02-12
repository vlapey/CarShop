from rest_framework import serializers
from .models import CarSpecification, Car


class CarSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSpecification
        exclude = ('is_active', )


class CarSerializer(serializers.ModelSerializer):
    specification = CarSpecificationSerializer()

    class Meta:
        model = Car
        exclude = ('is_active', 'customer', 'dealer', 'vendor')
