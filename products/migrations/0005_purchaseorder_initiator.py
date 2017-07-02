# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 03:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_auto_20170702_0138'),
        ('products', '0004_auto_20170702_0152'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='initiator',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='clients.Purchaser'),
        ),
    ]
