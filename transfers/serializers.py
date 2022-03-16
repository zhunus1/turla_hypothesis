from rest_framework import serializers
from django.utils.timezone import make_aware
from .models import (
    Transfer,
)
from rents.serializers import (
    UnixEpochDateField,
)


class TransferCreateSearializer(serializers.ModelSerializer):
    start_date = UnixEpochDateField()
    end_date = UnixEpochDateField()
    class Meta:
        model = Transfer
        fields = (
            'start_date',
            'end_date',
            'pick_up',
            'drop_off',
            'promo_code',   
        )
     
class TransferReturnSearializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = (
            'id',
            'total_cost',
            'total_cost_discount',  
        )
