# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-26 23:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('idjob', models.AutoField(primary_key=True, serialize=False)),
                ('jobname', models.CharField(max_length=20)),
                ('jobsalary', models.IntegerField()),
                ('jobtodo', models.CharField(max_length=45)),
                ('jobrules', models.CharField(max_length=45)),
            ],
        ),
    ]