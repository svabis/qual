# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapplot', '0022_auto_20210127_1018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mapplotimage',
            old_name='imgage',
            new_name='image',
        ),
    ]
