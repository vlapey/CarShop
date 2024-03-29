from rest_framework import routers

from src.car.views import CarViewSet
from src.customer.views import CustomerViewSet
from src.dealer.views import DealerViewSet
from src.vendor.views import VendorViewSet

from src.history.views import CustomerDealerHistoryViewSet, DealerVendorHistoryViewSet

from src.loyalties.views import DealersLoyaltiesViewSet, VendorLoyaltiesViewSet


def router_register():
    router = routers.DefaultRouter()
    router.register(r'car', CarViewSet)
    router.register(r'customer', CustomerViewSet)
    router.register(r'dealer', DealerViewSet)
    router.register(r'history', CustomerDealerHistoryViewSet)
    router.register(r'history', DealerVendorHistoryViewSet)
    router.register(r'loyalties', DealersLoyaltiesViewSet)
    router.register(r'loyalties', VendorLoyaltiesViewSet)
    router.register(r'vendor', VendorViewSet)

    return router
