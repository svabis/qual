# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kamera', '0012_auto_20170301_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bilde',
            name='bilde_nos',
            field=models.CharField(max_length=60),
        ),
    ]
