# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapplot', '0015_auto_20210127_0256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mapplot',
            name='radio',
        ),
    ]
