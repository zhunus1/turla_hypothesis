from django.db import models
from locations.models import (
    Location,
) 
from loyalties.models import (
    PromoCode,
) 

# Create your models here.
class Rent(models.Model):

    start_date = models.DateTimeField(
        verbose_name = "Start date",
    )

    end_date = models.DateTimeField(
        verbose_name = "End date",
    )

    location = models.ManyToManyField(
        verbose_name = "Pick up",
        to = Location,
        related_name = 'rents_pick_up',
    )

    promo_code = models.OneToOneField(
        verbose_name = "Promo code",
        to = PromoCode,
        related_name = 'rent',
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

        verbose_name = "Rent"
        verbose_name_plural = "Rents"
        ordering = ('-created',)
    
    @property
    def total_cost(self):
        return (self.end_date - self.start_date)//3600 * 250

    @property
    def total_cost_discount(self):
        return ((self.end_date - self.start_date)//3600 * 250) - 250