from django_filters import rest_framework as filters

from .models import Vendor


class VendorFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name')
    min_buyers_amount = filters.NumberFilter(field_name='buyers_amount', lookup_expr='gte')
    max_buyers_amount = filters.NumberFilter(field_name='buyers_amount', lookup_expr='lte')
    created_at = filters.DateTimeFromToRangeFilter(field_name='created_at')

    class Meta:
        model = Vendor
        fields = ['name', 'min_buyers_amount', 'max_buyers_amount', 'is_active', 'created_at']
