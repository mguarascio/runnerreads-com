# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reads', '0007_auto_20171115_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='link',
            field=models.CharField(max_length=2000),
        ),
    ]