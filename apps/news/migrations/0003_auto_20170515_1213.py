# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-15 04:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20170515_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newscomment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontuser.FrontUser', verbose_name='\u4f5c\u8005'),
        ),
    ]
