from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from rents.models import (
    Rent,
)
from transfers.models import (
    Transfer,
) 
# Create your models here.

class Customer(models.Model):

    name = models.CharField(
        max_length = 255,
        verbose_name = "Name",
    )

    phone_number = PhoneNumberField(
        verbose_name = "Phone number",
    )

    is_whatsapp = models.BooleanField(
        verbose_name = "Is whatsapp",
    )

    rent = models.OneToOneField(
        verbose_name = "Rent",
        to = Rent,
        related_name = 'customer_rent',
        on_delete = models.CASCADE,
        null = True,
        blank = True,
    )

    transfer = models.OneToOneField(
        verbose_name = "Transfer",
        to = Transfer,
        related_name = 'customer_transfer',
        on_delete = models.CASCADE,
        null = True,
        blank = True,
    )
    
    created = models.DateTimeField(
        verbose_name = "Created",
        auto_now_add = True,
    )

    updated = models.DateTimeField(
        verbose_name = "Updated",
        auto_now = True,
    )

    class Meta:

        verbose_name = "Customer"
        verbose_name_plural = "Customers"
        ordering = ('-created',)
        
    def __str__(self):
        return self.name
    