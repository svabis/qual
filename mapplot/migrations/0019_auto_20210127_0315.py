# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapplot', '0018_auto_20210127_0314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapplot',
            name='device',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
