# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0013_auto_20170301_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_data',
            name='user_last_visit',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
