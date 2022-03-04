# Generated by Django 4.0.3 on 2022-03-03 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loyalties', '0002_promorule_promocode_promo_rule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promocode',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='promorule',
            name='bonus_hours',
            field=models.TimeField(blank=True, null=True, verbose_name='Bonus hours'),
        ),
        migrations.AlterField(
            model_name='promorule',
            name='discount_percentage',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Discount percentage'),
        ),
        migrations.AlterField(
            model_name='promorule',
            name='required_hours',
            field=models.TimeField(blank=True, null=True, verbose_name='Required hours'),
        ),
    ]