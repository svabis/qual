# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kamera', '0022_auto_20170309_1345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bilde',
            name='bilde_visible',
        ),
        migrations.AlterField(
            model_name='kamera',
            name='kamera_slug',
            field=models.SlugField(default=b'WYRIqMDp', unique=True),
        ),
    ]
