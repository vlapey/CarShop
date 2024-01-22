from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from .models import DealersLoyalties, VendorsLoyalties
from .serializers import DealersLoyaltiesSerializer, VendorsLoyaltiesSerializer
from .filters import LoyaltiesFilter


class DealersLoyaltiesViewSet(mixins.ListModelMixin,
                              mixins.RetrieveModelMixin,
                              mixins.CreateModelMixin,
                              GenericViewSet):
    queryset = DealersLoyalties.objects.all()
    serializer_class = DealersLoyaltiesSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = LoyaltiesFilter


class VendorLoyaltiesViewSet(mixins.ListModelMixin,
                             mixins.RetrieveModelMixin,
                             mixins.CreateModelMixin,
                             GenericViewSet):
    queryset = VendorsLoyalties.objects.all()
    serializer_class = VendorsLoyaltiesSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = LoyaltiesFilter
