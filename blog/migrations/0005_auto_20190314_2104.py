# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-03-14 21:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_prods'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Prods',
            new_name='Product',
        ),
    ]
