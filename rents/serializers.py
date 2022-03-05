from rest_framework import serializers
from django.utils.timezone import make_aware
from .models import (
    Rent,
)

class UnixEpochDateField(serializers.DateTimeField):
    def to_representation(self, value):
        import time
        try:
            return int(time.mktime(value.timetuple()))
        except (AttributeError, TypeError):
            return None

    def to_internal_value(self, value):
        from datetime import datetime
        return make_aware(datetime.fromtimestamp(int(value)/1000))

class RentCreateSearializer(serializers.ModelSerializer):
    start_date = UnixEpochDateField()
    end_date = UnixEpochDateField()
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