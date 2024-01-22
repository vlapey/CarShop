from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .filters import CarsFilter

from .models import Cars, CarSpecification
from .serializers import CarSerializer, CarSpecificationSerializer


class CarViewSet(mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.CreateModelMixin,
                 GenericViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CarsFilter


class CarSpecificationViewSet(mixins.ListModelMixin,
                              mixins.RetrieveModelMixin,
                              mixins.CreateModelMixin,
                              GenericViewSet):
    queryset = CarSpecification.objects.all()
    serializer_class = CarSpecificationSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
