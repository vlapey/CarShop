from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from .models import CustomerDealerHistory, DealerVendorHistory
from .serializers import CustomerDealerHistorySerializer, DealerVendorHistorySerializer


class CustomerDealerHistoryViewSet(mixins.ListModelMixin,
                                   mixins.RetrieveModelMixin,
                                   mixins.CreateModelMixin,
                                   GenericViewSet):
    queryset = CustomerDealerHistory.objects.all()
    serializer_class = CustomerDealerHistorySerializer


class DealerVendorHistoryViewSet(mixins.ListModelMixin,
                                 mixins.RetrieveModelMixin,
                                 mixins.CreateModelMixin,
                                 GenericViewSet):
    queryset = DealerVendorHistory.objects.all()
    serializer_class = DealerVendorHistorySerializer
