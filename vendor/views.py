from rest_framework import generics
from rest_framework import mixins
from .models import Vendor
from .serializers import VendorSerializer


class VendorViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                    generics.GenericAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
