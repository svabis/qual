# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kamera', '0002_bilde_bilde_kamera_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bilde',
            old_name='bilde_kamera_id',
            new_name='bilde_kamera',
        ),
    ]
