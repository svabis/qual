# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import galerija.models


class Migration(migrations.Migration):

    dependencies = [
        ('galerija', '0002_auto_20170911_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galerija',
            name='bilde_bilde',
            field=models.ImageField(null=True, upload_to=galerija.models.image_file_path, blank=True),
        ),
        migrations.AlterField(
            model_name='galerija',
            name='bilde_thumb',
            field=models.ImageField(null=True, upload_to=galerija.models.thumb_file_path, blank=True),
        ),
    ]
