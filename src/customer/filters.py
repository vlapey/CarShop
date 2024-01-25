from django_filters import rest_framework as filters

from .models import Customer


class CustomerFilter(filters.FilterSet):
    last_name = filters.CharFilter(field_name='last_name')
    is_active = filters.BooleanFilter(field_name='is_active')
    date_created = filters.DateTimeFromToRangeFilter(field_name='date_created')

    class Meta:
        model = Customer
        fields = ['last_name', 'is_active', 'date_created']
