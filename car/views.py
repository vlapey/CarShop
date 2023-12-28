from rest_framework import generics
from rest_framework import mixins
from .models import Car
from .serializers import CarSerializer


class CarViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                 generics.GenericAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
