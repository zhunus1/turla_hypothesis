from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from geopy.geocoders import Nominatim
from django.http import Http404
from rest_framework import status
from rest_framework.decorators import action
from .models import (
    Transfer,
)
from .serializers import (
    TransferCreateSearializer,
    TransferReturnSearializer,
)

# Create your views here.

class TransferView(APIView):

    def post(self, request):
        serializer = TransferCreateSearializer(data=request.data)
        if serializer.is_valid():
            rent = serializer.save()
            return Response(TransferReturnSearializer(rent).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)