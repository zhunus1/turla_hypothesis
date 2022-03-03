from django.db import models

# Create your models here.
class PromoCode(models.Model):

    code = models.CharField(
        max_length=255,
        verbose_name = "Code",
    )   

    description = models.TextField(
        verbose_name = "Description",
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