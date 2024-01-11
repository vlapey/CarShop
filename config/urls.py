"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from src.cars.views import CarViewSet
from src.customer.views import CustomerViewSet
from src.dealer.views import DealerViewSet
from src.history.views import CustomerDealerHistoryViewSet
from src.history.views import DealerVendorHistoryViewSet
from src.loyalties.views import DealersLoyaltiesViewSet
from src.loyalties.views import VendorLoyaltiesViewSet
from src.orders.views import CustomerOrderViewSet
from src.orders.views import DealerOrderViewSet
from src.vendor.views import VendorViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cars', CarViewSet)
router.register(r'customer', CustomerViewSet)
router.register(r'dealer', DealerViewSet)
router.register(r'history', CustomerDealerHistoryViewSet)
router.register(r'history', DealerVendorHistoryViewSet)
router.register(r'loyalties', DealersLoyaltiesViewSet)
router.register(r'loyalties', VendorLoyaltiesViewSet)
router.register(r'orders', CustomerOrderViewSet)
router.register(r'orders', DealerOrderViewSet)
router.register(r'vendor', VendorViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
