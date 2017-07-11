# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-03 11:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tables', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('idworker', models.AutoField(primary_key=True, serialize=False)),
                ('workername', models.CharField(max_length=50)),
                ('workerage', models.IntegerField(default=20)),
                ('workergender', models.CharField(max_length=10)),
                ('workeraddress', models.CharField(max_length=50)),
                ('workerpass', models.CharField(max_length=70)),
                ('workerjob', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tables.Jobs')),
            ],
        ),
    ]