# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kamera', '0046_auto_20200115_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kamera',
            name='kamera_apraksts',
            field=models.TextField(default=b'', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='kamera',
            name='kamera_slug',
            field=models.SlugField(default=b'598d3135d39c', unique=True),
        ),
    ]
