import django_filters as filters
from .models import Location

class LocationFilter(filters.FilterSet):
    region = filters.CharFilter(field_name='region__name')

    class Meta:
        model = Location
        fields = (
            'region',
        )