from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import (
    RentViewSet,
)

router = DefaultRouter()
router.register(r'rent', RentViewSet, basename='rent')

urlpatterns = [] + router.urls
