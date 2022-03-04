from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import (
    RentView,
)

urlpatterns = [
    path('rent/', RentView.as_view()),
]
