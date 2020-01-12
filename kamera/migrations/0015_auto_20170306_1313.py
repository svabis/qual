# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kamera', '0014_auto_20170304_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kamera',
            name='kamera_slug',
            field=models.SlugField(default=b'ycGuyXGG', unique=True),
        ),
    ]
