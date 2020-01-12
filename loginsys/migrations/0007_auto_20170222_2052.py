# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0006_user_kamera'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_kamera',
            name='kamera',
        ),
        migrations.RemoveField(
            model_name='user_kamera',
            name='user',
        ),
        migrations.DeleteModel(
            name='User_kamera',
        ),
    ]
