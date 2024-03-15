from django_filters import rest_framework as filters

from .models import Loyalties


class LoyaltiesFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name')
    min_discount = filters.NumberFilter(field_name='discount', lookup_expr='gte')
    max_discount = filters.NumberFilter(field_name='discount', lookup_expr='lte')
    is_active = filters.BooleanFilter(field_name='is_active')
    created_at = filters.DateTimeFromToRangeFilter(field_name='created_at')

    class Meta:
        model = Loyalties
        fields = ['name', 'min_discount', 'max_discount', 'is_active', 'created_at']
