# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galerija', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galerija',
            name='bilde_bilde',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='galerija',
            name='bilde_thumb',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
    ]
