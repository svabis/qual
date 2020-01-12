# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kamera', '0041_auto_20191218_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kamera',
            name='kamera_slug',
            field=models.SlugField(default=b'27d71646877d', unique=True),
        ),
    ]
