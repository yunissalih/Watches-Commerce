# Generated by Django 3.0.5 on 2022-09-18 01:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_listings_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='watchlisters',
            field=models.ManyToManyField(blank=True, related_name='watchlist', to=settings.AUTH_USER_MODEL),
        ),
    ]
