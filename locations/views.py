from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from geopy.geocoders import Nominatim
from django.http import Http404
from rest_framework import status
from rest_framework.decorators import action
from .models import (
    Location,
    Region,
)
from .serializers import (
    LocationSearializer,
    RegionSearializer,
    GeoSearializer,
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
    
    @action(methods=['POST'], detail=False)    
    def find_location(self, request):
        serializer = GeoSearializer(data=request.data)
        if serializer.is_valid():
            geolocator = Nominatim(user_agent="turla_hypothesis")
            location = geolocator.reverse(serializer.validated_data['coordinates'])
            return Response(location.raw['address'], status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSearializer