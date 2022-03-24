from django.db import models
from locations.models import (
    Location,
) 
from loyalties.models import (
    PromoCode,
) 

# Create your models here.
class Transfer(models.Model):

    start_date = models.DateTimeField(
        verbose_name = "Start date",
    )

    end_date = models.DateTimeField(
        verbose_name = "End date",
    )

    pick_up = models.CharField(
        verbose_name = "Pick up",
        max_length = 255,
    )

    drop_off = models.ForeignKey(
        verbose_name = "Drop off",
        to = Location,
        on_delete = models.CASCADE,
        related_name = 'transfers',
        blank = True,
    )

    promo_code = models.ForeignKey(
        verbose_name = "Promo code",
        to = PromoCode,
        related_name = 'transfers',
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

        verbose_name = "Transfer"
        verbose_name_plural = "Transfers"
        ordering = ('-created',)
    
    @property
    def total_cost(self):
        return ((self.end_date - self.start_date).total_seconds()//3600) * 250

    @property
    def total_cost_discount(self):
        return (((self.end_date - self.start_date).total_seconds()//3600) * 250) - 250