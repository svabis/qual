# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kamera', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bilde',
            name='bilde_kamera_id',
            field=models.ForeignKey(default=1, to='kamera.Kamera'),
        ),
    ]
