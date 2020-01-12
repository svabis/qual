# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kamera', '0006_kamera_kamera_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='bilde',
            name='bilde_patik',
            field=models.IntegerField(default=0),
        ),
    ]
