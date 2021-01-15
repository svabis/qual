# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapplot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapplot',
            name='mark',
            field=models.CharField(default=b'', max_length=8, blank=True),
        ),
        migrations.AlterField(
            model_name='mapplot',
            name='radio',
            field=models.CharField(default=b'green', max_length=10, choices=[(b'green', b'stabs'), (b'red', b'kaste')]),
        ),
    ]
