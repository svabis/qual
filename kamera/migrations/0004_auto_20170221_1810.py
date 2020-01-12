# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kamera', '0003_auto_20170221_1808'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bilde',
            old_name='bilde_kamera',
            new_name='bilde_kamera_id',
        ),
    ]
