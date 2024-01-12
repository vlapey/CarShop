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
        fields = ('id', 'brand', 'specification', 'car_type', 'color')

    def create(self, validated_data):
        specification_data = validated_data.pop('specification')
        specification = CarSpecification.objects.get_or_create(**specification_data)
        cars = Cars.objects.create(specification=specification[0], **validated_data)

        return cars
