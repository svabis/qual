# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('galerija', '0004_auto_20171109_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='galerijakoment',
            name='koment_datums',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
