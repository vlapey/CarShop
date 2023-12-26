from rest_framework import serializers
from .models import CarSpecification, Car


class CarSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSpecification
        fields = ('id', 'name', 'engine', 'horsepower', 'torque')


class CarSerializer(serializers.ModelSerializer):
    specification = CarSpecificationSerializer()

    class Meta:
        model = Car
        fields = ('id', 'model', 'specification', 'time_created')
