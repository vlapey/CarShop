from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from .models import CustomerOrder, DealerOrder
from .serializers import CustomerOrderSerializer, DealerOrderSerializer


class CustomerOrderViewSet(mixins.ListModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.CreateModelMixin,
                           GenericViewSet):
    queryset = CustomerOrder.objects.all()
    serializer_class = CustomerOrderSerializer


class DealerOrderViewSet(mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.CreateModelMixin,
                         GenericViewSet):
    queryset = DealerOrder.objects.all()
    serializer_class = DealerOrderSerializer