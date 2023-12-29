from rest_framework import generics
from rest_framework import mixins
from .models import Customer
from .serializers import CustomerSerializer


class CustomerViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
