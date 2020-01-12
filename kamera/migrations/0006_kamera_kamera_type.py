# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kamera', '0005_remove_bilde_bilde_visible'),
    ]

    operations = [
        migrations.AddField(
            model_name='kamera',
            name='kamera_type',
            field=models.CharField(default=b'PUB', max_length=10, choices=[(b'PUB', b'public'), (b'PRIV', b'private'), (b'SHARE', b'share')]),
        ),
    ]
