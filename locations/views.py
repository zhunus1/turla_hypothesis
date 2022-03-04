from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from .models import (
    Location,
)
from .serializers import (
    LocationSearializer,
)

# Create your views here.
class LocationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSearializer
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'region__name')