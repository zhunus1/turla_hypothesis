from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import (
    Rent,
)
from .serializers import (
    RentSearializer,
)

# Create your views here.

class RentViewSet(viewsets.ModelViewSet):
    
    queryset = Rent.objects.all()
    serializer_class = RentSearializer