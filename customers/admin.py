from django.contrib import admin
from .models import (
    Customer,
)

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    pass

# Register the admin class with the associated model
admin.site.register(Customer, CustomerAdmin)