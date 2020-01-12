# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('galerija', '0006_galerijalike'),
    ]

    operations = [
        migrations.AddField(
            model_name='galerijalike',
            name='last_entry',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
