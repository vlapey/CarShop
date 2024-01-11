from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from .models import DealersLoyalties, VendorsLoyalties
from .serializers import DealersLoyaltiesSerializer, VendorsLoyaltiesSerializer


class DealersLoyaltiesViewSet(mixins.ListModelMixin,
                              mixins.RetrieveModelMixin,
                              mixins.CreateModelMixin,
                              GenericViewSet):
    queryset = DealersLoyalties.objects.all()
    serializer_class = DealersLoyaltiesSerializer


class VendorLoyaltiesViewSet(mixins.ListModelMixin,
                             mixins.RetrieveModelMixin,
                             mixins.CreateModelMixin,
                             GenericViewSet):
    queryset = VendorsLoyalties.objects.all()
    serializer_class = VendorsLoyaltiesSerializer
