# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 06:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('phone', models.CharField(default='', max_length=20)),
                ('email', models.CharField(default='', max_length=20)),
                ('price', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('image', models.CharField(default='', max_length=20)),
                ('category', models.CharField(default='', max_length=20)),
                ('location', models.CharField(default='', max_length=20)),
                ('amount', models.CharField(default='', max_length=20)),
                ('purchaser', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='clients.Purchaser')),
            ],
        ),
        migrations.AddField(
            model_name='postprice',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
    ]
