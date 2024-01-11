from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from .models import Vendor
from .serializers import VendorSerializer


class VendorViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    GenericViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
