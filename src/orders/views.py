from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from .models import CustomerOrder, DealerOrder
from .serializers import CustomerOrderSerializer, DealerOrderSerializer
from .filters import CustomerOrderFilter, DealerOrderFilter


class CustomerOrderViewSet(mixins.ListModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.CreateModelMixin,
                           GenericViewSet):
    queryset = CustomerOrder.objects.all()
    serializer_class = CustomerOrderSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CustomerOrderFilter


class DealerOrderViewSet(mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.CreateModelMixin,
                         GenericViewSet):
    queryset = DealerOrder.objects.all()
    serializer_class = DealerOrderSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = DealerOrderFilter
