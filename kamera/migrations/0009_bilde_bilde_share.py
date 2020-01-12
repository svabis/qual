# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kamera', '0008_bilde_bilde_visible'),
    ]

    operations = [
        migrations.AddField(
            model_name='bilde',
            name='bilde_share',
            field=models.BooleanField(default=False),
        ),
    ]
