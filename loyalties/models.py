from django.db import models

# Create your models here.
class PromoRule(models.Model):
    class PromoType(models.TextChoices):
        min_hours = 'Min hours', ('Min hours')
        first_hours = 'First hours', ('First hours')
        additional_hours = 'Additional hours', ('Additional hours')
        fixed = 'Fixed discount', ('Fixed discount')

    promo_type = models.CharField(
        max_length=63,
        choices=PromoType.choices,
        verbose_name = "Promo type",
    )

    required_hours = models.TimeField(
        verbose_name = "Required hours",
        null = True,
        blank = True,
    )

    bonus_hours = models.TimeField(
        verbose_name = "Bonus hours",
        null = True,
        blank = True,
    )

    discount_percentage = models.PositiveSmallIntegerField(
        verbose_name = "Discount percentage",
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

        verbose_name = "Promo rule"
        verbose_name_plural = "Promo rules"
        ordering = ('-created',)
        
    def __str__(self):
        return self.promo_type

class PromoCode(models.Model):

    code = models.CharField(
        max_length=255,
        verbose_name = "Code",
    )   

    description = models.TextField(
        verbose_name = "Description",
        null = True,
        blank = True,
    )

    promo_rule = models.ForeignKey(
        to = PromoRule, 
        on_delete = models.CASCADE,
        related_name = 'promo_codes',
        verbose_name = "Promo rule",
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

        verbose_name = "Promo code"
        verbose_name_plural = "Promo codes"
        ordering = ('-created',)
        
    def __str__(self):
        return self.code