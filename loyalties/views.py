from rest_framework import generics
from rest_framework import mixins
from .models import DealersLoyalties, VendorsLoyalties
from .serializers import DealersLoyaltiesSerializer, VendorsLoyaltiesSerializer


class DealersLoyaltiesViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                              mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = DealersLoyalties.objects.all()
    serializer_class = DealersLoyaltiesSerializer


class VendorLoyaltiesViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                             mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = VendorsLoyalties.objects.all()
    serializer_class = VendorsLoyaltiesSerializer
