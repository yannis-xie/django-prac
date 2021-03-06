# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-04 13:34
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0002_auto_20171227_1654'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlepost',
            options={'ordering': ('-updated',)},
        ),
        migrations.AddField(
            model_name='articlepost',
            name='users_like',
            field=models.ManyToManyField(blank=True, related_name='articles_like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 4, 13, 34, 32, 821000, tzinfo=utc)),
        ),
    ]
