# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kamera', '0045_auto_20200112_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='kamera',
            name='kamera_ftp',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='kamera',
            name='kamera_slug',
            field=models.SlugField(default=b'0613695cc375', unique=True),
        ),
    ]
