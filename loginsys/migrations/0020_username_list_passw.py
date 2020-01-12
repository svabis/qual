# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0019_username_list_kamera_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='username_list',
            name='passw',
            field=models.CharField(default=b'', max_length=30),
        ),
    ]
