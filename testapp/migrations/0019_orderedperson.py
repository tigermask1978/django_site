# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-13 02:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0018_auto_20170613_1035'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderedPerson',
            fields=[
            ],
            options={
                'ordering': ['last_name'],
                'proxy': True,
                'indexes': [],
            },
            bases=('testapp.person',),
        ),
    ]
