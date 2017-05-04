# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 16:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('surname', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateField(blank=True, null=True)),
                ('doi', models.CharField(blank=True, max_length=60)),
                ('imported_datetime', models.DateTimeField(auto_now_add=True, null=True)),
                ('authors', models.ManyToManyField(blank=True, to='publications.Author')),
            ],
        ),
    ]
