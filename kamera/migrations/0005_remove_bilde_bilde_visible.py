# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kamera', '0004_auto_20170221_1810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bilde',
            name='bilde_visible',
        ),
    ]
