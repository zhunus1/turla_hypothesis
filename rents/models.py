from django.db import models
from locations.models import (
    Location,
) 
from loyalties.models import (
    PromoCode,
) 
from customers.models import (
    Customer,
) 

# Create your models here.
class Rent(models.Model):

    customer = models.ForeignKey(
        verbose_name = "Customer",
        to = Customer,
        related_name = 'rents',
        on_delete = models.CASCADE,
    )

    start_date = models.DateTimeField(
        verbose_name = "Start date",
        blank = True,
        null = True
    )

    end_date = models.DateTimeField(
        verbose_name = "End date",
        blank = True,
        null = True
    )

    pick_up = models.ManyToManyField(
        verbose_name = "Pick up",
        to = Location,
        related_name = 'rents_pick_up',
    )

    drop_off = models.ManyToManyField(
        verbose_name = "Drop off",
        to = Location,
        related_name = 'rents_drop_off',
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
        
    def __str__(self):
        return '%s - %s' % (self.customer.name, self.customer.phone_number)
    
    @property
    def total_cost(self):
        return (self.start_date - self.end_date).hours * 250

    @property
    def total_cost_discount(self):
        try:
            promo_rule = self.promo_code.promo_rule
            if promo_rule.promo_type == 'Min hours':
                difference = (self.start_date - self.end_date).hours
                if difference > self.promo_code.required_hours:
                    return ((self.start_date - self.end_date).hours * 250) - (self.promo_code.bonus_hours * 250)
            elif promo_rule.promo_type == 'First hours':
                difference = (self.start_date - self.end_date).hours
                return (self.promo_code.bonus_hours * 125) + (difference - self.promo_code.bonus_hours) * 250
            elif promo_rule.promo_type == 'Additional hours':
                return ((self.start_date - self.end_date).hours * 250) - (self.promo_code.bonus_hours * 250)
            else:
                return ((self.start_date - self.end_date).hours * 250) * (self.promo_code.discount_percentage/100)
        except:
            return (self.start_date - self.end_date).hours * 250