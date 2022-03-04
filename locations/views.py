from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import (
    Location,
)
from .serializers import (
    LocationSearializer,
)
from .filters import (
    LocationFilter,
)

# Create your views here.
class LocationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSearializer
    filter_backends = (SearchFilter, DjangoFilterBackend,)
    search_fields = ('name', 'region__name')
    filter_class = LocationFilter