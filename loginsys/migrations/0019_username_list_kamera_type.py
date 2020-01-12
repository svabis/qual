# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0018_username_list_kamera'),
    ]

    operations = [
        migrations.AddField(
            model_name='username_list',
            name='kamera_type',
            field=models.CharField(default=b'PUB', max_length=6),
        ),
    ]
