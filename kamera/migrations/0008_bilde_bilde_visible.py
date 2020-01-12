# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kamera', '0007_bilde_bilde_patik'),
    ]

    operations = [
        migrations.AddField(
            model_name='bilde',
            name='bilde_visible',
            field=models.BooleanField(default=True),
        ),
    ]
