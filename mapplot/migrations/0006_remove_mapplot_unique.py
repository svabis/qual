# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapplot', '0005_mapplotimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mapplot',
            name='unique',
        ),
    ]
