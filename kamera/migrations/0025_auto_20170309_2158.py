# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kamera', '0024_auto_20170309_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kamera',
            name='kamera_slug',
            field=models.SlugField(default=b'GHBzGyMN', unique=True),
        ),
    ]
