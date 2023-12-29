from rest_framework import generics
from rest_framework import mixins
from .models import CustomerDealerHistory, DealerVendorHistory
from .serializers import CustomerDealerHistorySerializer, DealerVendorHistorySerializer


class CustomerDealerHistoryViewSet(mixins.ListModelMixin,
                                   mixins.RetrieveModelMixin,
                                   mixins.CreateModelMixin,
                                   generics.GenericAPIView):
    queryset = CustomerDealerHistory
    serializer_class = CustomerDealerHistorySerializer


class DealerVendorHistoryViewSet(mixins.ListModelMixin,
                                 mixins.RetrieveModelMixin,
                                 mixins.CreateModelMixin,
                                 generics.GenericAPIView):
    queryset = DealerVendorHistory
    serializer_class = DealerVendorHistorySerializer
