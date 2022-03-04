from rest_framework import serializers
from .models import (
    Country,
    Region,
    Location,
)

class LocationSearializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = (
            'id',
            'name',
        )
