# Generated by Django 4.0.3 on 2022-03-04 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loyalties', '0003_alter_promocode_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='promocode',
            name='promo_rule',
        ),
        migrations.DeleteModel(
            name='PromoRule',
        ),
    ]
