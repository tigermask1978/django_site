# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-07 11:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0008_auto_20170607_1915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='sub_orgnizations',
        ),
        migrations.AddField(
            model_name='organization',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='suborganizations', to='testapp.Organization'),
        ),
    ]
