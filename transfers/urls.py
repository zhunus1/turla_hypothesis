from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import (
    TransferView,
)

urlpatterns = [
    path('transfer/', TransferView.as_view()),
]
