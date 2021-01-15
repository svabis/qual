# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapplot', '0007_auto_20210106_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapplotcity',
            name='name',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
