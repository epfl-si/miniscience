# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 12:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0003_publication_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='sciper',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]