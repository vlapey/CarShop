from rest_framework import serializers
from .models import CarSpecification, Cars


class CarSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSpecification
        fields = ('id', 'name', 'engine', 'horsepower', 'torque')


class CarSerializer(serializers.ModelSerializer):
    specification = CarSpecificationSerializer()

    class Meta:
        model = Cars
        fields = ('id', 'specification', 'color', 'mileage')
