# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 06:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20170702_0513'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseofferline',
            name='is_noticed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='purchaseofferline',
            name='is_updated',
            field=models.BooleanField(default=True),
        ),
    ]
