# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-16 08:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0022_themeblog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('num_awards', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('registered_users', models.PositiveIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='bookreview',
            name='article_ptr',
        ),
        migrations.RemoveField(
            model_name='bookreview',
            name='book_ptr',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='book_id',
            new_name='id',
        ),
        migrations.AddField(
            model_name='author',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='testapp.Author'),
        ),
        migrations.AddField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='pages',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='pubdate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='rating',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='BookReview',
        ),
        migrations.AddField(
            model_name='store',
            name='books',
            field=models.ManyToManyField(to='testapp.Book'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='testapp.Publisher'),
        ),
    ]
