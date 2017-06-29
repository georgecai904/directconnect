# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 09:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20170627_0648'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(default='', max_length=20)),
                ('name', models.CharField(default='', max_length=20)),
                ('phone', models.CharField(default='', max_length=20)),
                ('email', models.CharField(default='', max_length=20)),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
    ]