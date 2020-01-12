# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0012_auto_20170224_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_kamera',
            name='kamera',
            field=models.ForeignKey(related_name='kam', to='kamera.Kamera'),
        ),
    ]
