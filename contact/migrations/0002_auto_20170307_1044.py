# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(max_length=255),
        ),
    ]
