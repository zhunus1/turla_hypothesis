from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import (
    LocationViewSet,
    RegionViewSet
)

router = DefaultRouter()
router.register(r'location', LocationViewSet, basename='location')
router.register(r'region', RegionViewSet, basename='region')

urlpatterns = [] + router.urls
