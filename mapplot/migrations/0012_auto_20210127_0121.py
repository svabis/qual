# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapplot', '0011_mapplotusercity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapplot',
            name='mark',
            field=models.CharField(default=b'', max_length=12),
        ),
    ]
