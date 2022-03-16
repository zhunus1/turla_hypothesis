# Generated by Django 4.0.3 on 2022-03-16 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rents', '0003_alter_rent_promo_code'),
        ('transfers', '0001_initial'),
        ('customers', '0006_alter_customer_rent_alter_customer_transfer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='rent',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_rent', to='rents.rent', verbose_name='Rent'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='transfer',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_transfer', to='transfers.transfer', verbose_name='Transfer'),
        ),
    ]
