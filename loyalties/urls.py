from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import (
    PromoCodeViewSet,
)

router = DefaultRouter()
router.register(r'promocode', PromoCodeViewSet, basename='promocode')

urlpatterns = [] + router.urls
