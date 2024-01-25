from rest_framework import serializers
from .models import CarSpecification, Cars


class CarSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSpecification
        exclude = ('is_active', )


class CarSerializer(serializers.ModelSerializer):
    specification = CarSpecificationSerializer()

    class Meta:
        model = Cars
        exclude = ('is_active', 'customer', 'dealer', 'vendor')
