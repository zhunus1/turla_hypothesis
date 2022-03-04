from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from .models import (
    Customer,
)
from .serializers import (
    CustomerSerializer,
)

# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
