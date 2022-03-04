from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from .models import (
    Rent,
)
from .serializers import (
    RentCreateSearializer,
    RentReturnSearializer
)

# Create your views here.

class RentView(APIView):

    def post(self, request):
        serializer = RentCreateSearializer(data=request.data)
        if serializer.is_valid():
            rent = serializer.save()
            return Response(RentReturnSearializer(rent).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
