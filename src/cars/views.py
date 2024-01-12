from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .models import Cars, CarSpecification
from .serializers import CarSerializer, CarSpecificationSerializer


class CarViewSet(mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.CreateModelMixin,
                 GenericViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarSerializer


class CarSpecificationViewSet(mixins.ListModelMixin,
                              mixins.RetrieveModelMixin,
                              mixins.CreateModelMixin,
                              GenericViewSet):
    queryset = CarSpecification.objects.all()
    serializer_class = CarSpecificationSerializer
