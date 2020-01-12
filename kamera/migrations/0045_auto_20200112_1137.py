# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kamera', '0044_auto_20200111_0758'),
    ]

    operations = [
        migrations.AddField(
            model_name='kamera',
            name='kamera_ai',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='kamera',
            name='kamera_slug',
            field=models.SlugField(default=b'dae429d9b025', unique=True),
        ),
    ]
