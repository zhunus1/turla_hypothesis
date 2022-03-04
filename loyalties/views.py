from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from .models import (
    PromoCode,
)
from .serializers import (
    PromoCodeSerializer,
)

# Create your views here.
class PromoCodeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PromoCode.objects.all()
    serializer_class = PromoCodeSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('code',)