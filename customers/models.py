from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Customer(models.Model):

    name = models.CharField(
        max_length = 255,
        verbose_name = "Name",
    )

    phone_number = PhoneNumberField()
    
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