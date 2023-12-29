from rest_framework import generics
from rest_framework import mixins
from .models import Dealer
from .serializers import DealerSerializer


class DealerViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer
