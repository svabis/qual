# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kamera', '0009_bilde_bilde_share'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bilde',
            name='bilde_patik',
        ),
    ]
