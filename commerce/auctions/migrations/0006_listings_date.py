# Generated by Django 3.0.5 on 2022-09-15 01:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20220915_0409'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
