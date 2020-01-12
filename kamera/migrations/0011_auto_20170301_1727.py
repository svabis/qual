# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kamera', '0010_remove_bilde_bilde_patik'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bilde',
            name='bilde_nos',
            field=models.CharField(unique=True, max_length=50),
        ),
    ]
