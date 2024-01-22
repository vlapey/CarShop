from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from .models import Dealer
from .serializers import DealerSerializer
from .filters import DealerFilter


class DealerViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    GenericViewSet):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = DealerFilter
