from rest_framework import serializers
from .models import (
    Rent,
)

class RentSearializer(serializers.ModelSerializer):
    class Meta:
        model = Rent
        fields = (
            'start_date',
            'end_date',
            'pick_up',
            'drop_off',
            'promo_code',   
        )
 