# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import galerija.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Galerija',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bilde_nos', models.CharField(max_length=60)),
                ('bilde_bilde', models.ImageField(null=True, upload_to=galerija.models.image_file_path, blank=True)),
                ('bilde_thumb', models.ImageField(null=True, upload_to=galerija.models.thumb_file_path, blank=True)),
                ('bilde_datums', models.DateTimeField(default=django.utils.timezone.now)),
                ('bilde_added', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'galerija',
            },
        ),
    ]
