# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mapplot.models


class Migration(migrations.Migration):

    dependencies = [
        ('mapplot', '0003_auto_20210106_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapplot',
            name='mark',
#            field=models.CharField(default=b'', max_length=8, validators=[mapplot.models.validate_point]),
            field=models.CharField(default=b'', max_length=8,), # validators=[mapplot.models.validate_point]),
        ),
    ]
