from django_filters import rest_framework as filters

from .models import Cars


class CarsFilter(filters.FilterSet):
    min_horsepower = filters.NumberFilter(field_name='specification__horsepower', lookup_expr='gte')
    max_horsepower = filters.NumberFilter(field_name='specification__horsepower', lookup_expr='lte')
    is_active = filters.BooleanFilter(field_name='is_active')
    date_created = filters.DateTimeFromToRangeFilter(field_name='date_created')

    class Meta:
        model = Cars
        fields = ['min_horsepower', 'max_horsepower', 'is_active', 'date_created']