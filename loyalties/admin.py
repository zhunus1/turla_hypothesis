from django.contrib import admin
from .models import (
    PromoRule,
    PromoCode,
) 

# Register your models here.
admin.site.register(PromoRule)
admin.site.register(PromoCode)