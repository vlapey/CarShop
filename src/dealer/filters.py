from django_filters import rest_framework as filters

from .models import Dealer


class DealerFilter(filters.FilterSet):
    location = filters.CharFilter(field_name='location')
    is_active = filters.BooleanFilter(field_name='is_active')
    date_created = filters.DateTimeFromToRangeFilter(field_name='date_created')

    class Meta:
        model = Dealer
        fields = ['location', 'is_active', 'date_created']