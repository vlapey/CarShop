from django_filters import rest_framework as filters

from .models import CustomerOrder, DealerOrder


class CustomerOrderFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')
    is_active = filters.BooleanFilter(field_name='is_active')
    date_created = filters.DateTimeFromToRangeFilter(field_name='date_created')

    class Meta:
        model = CustomerOrder
        fields = ['min_price', 'max_price', 'is_active', 'date_created']


class DealerOrderFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')
    is_active = filters.BooleanFilter(field_name='is_active')
    created_at = filters.DateTimeFromToRangeFilter(field_name='date_created')

    class Meta:
        model = DealerOrder
        fields = ['min_price', 'max_price', 'is_active', 'date_created']