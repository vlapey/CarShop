from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from .models import Dealer
from .serializers import DealerSerializer


class DealerViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    GenericViewSet):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer
