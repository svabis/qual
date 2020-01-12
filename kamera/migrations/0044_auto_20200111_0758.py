# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kamera', '0043_auto_20191218_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kamera',
            name='kamera_apraksts',
            field=models.TextField(default=b'kameras apraksts', blank=True),
        ),
        migrations.AlterField(
            model_name='kamera',
            name='kamera_slug',
            field=models.SlugField(default=b'381104bab63b', unique=True),
        ),
    ]
