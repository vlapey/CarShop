from django_filters import rest_framework as filters

from .models import Loyalties


class LoyaltiesFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name')
    min_discount = filters.NumberFilter(field_name='discount', lookup_expr='gte')
    max_discount = filters.NumberFilter(field_name='discount', lookup_expr='lte')
    is_active = filters.BooleanFilter(field_name='is_active')
    date_created = filters.DateTimeFromToRangeFilter(field_name='date_created')

    class Meta:
        model = Loyalties
        fields = ['name', 'min_discount', 'max_discount', 'is_active', 'date_created']
