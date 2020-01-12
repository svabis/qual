# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0009_user_kamera'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_kamera',
            name='kamera',
            field=models.ForeignKey(to='kamera.Kamera'),
        ),
    ]
