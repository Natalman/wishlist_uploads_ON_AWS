# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 01:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_wishlist', '0004_auto_20170227_2303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='days_since_visited',
        ),
        migrations.AlterField(
            model_name='place',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
