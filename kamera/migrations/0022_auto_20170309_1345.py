# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kamera', '0021_auto_20170308_2240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bilde',
            name='bilde_share',
        ),
        migrations.AlterField(
            model_name='kamera',
            name='kamera_slug',
            field=models.SlugField(default=b'pJmVVxaQ', unique=True),
        ),
    ]
