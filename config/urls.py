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
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from src.cars.views import CarViewSet
from src.customer.views import CustomerViewSet
from src.dealer.views import DealerViewSet
from src.vendor.views import VendorViewSet

from src.history.views import CustomerDealerHistoryViewSet, DealerVendorHistoryViewSet

from src.loyalties.views import DealersLoyaltiesViewSet, VendorLoyaltiesViewSet

from src.orders.views import CustomerOrderViewSet, DealerOrderViewSet

from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="Vlad",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

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

api_auth = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/auth/', include(api_auth)),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("__debug__/", include("debug_toolbar.urls")),
]


