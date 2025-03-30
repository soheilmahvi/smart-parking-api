# parking/filters.py

import django_filters
from .models import ParkingSpot

class ParkingSpotFilter(django_filters.FilterSet):
    is_reserved = django_filters.BooleanFilter()
    garage = django_filters.NumberFilter()
    number_min = django_filters.NumberFilter(field_name='number', lookup_expr='gte')
    number_max = django_filters.NumberFilter(field_name='number', lookup_expr='lte')

    class Meta:
        model = ParkingSpot
        fields = ['is_reserved', 'garage', 'number_min', 'number_max']
