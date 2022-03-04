from rest_framework import serializers
from .models import (
    Rent,
)


class RentCreateSearializer(serializers.ModelSerializer):
    class Meta:
        model = Rent
        fields = (
            'start_date',
            'end_date',
            'location',
            'promo_code',   
        )
     
class RentReturnSearializer(serializers.ModelSerializer):
    class Meta:
        model = Rent
        fields = (
            'id',
            'total_cost',
            'total_cost_discount',  
        )