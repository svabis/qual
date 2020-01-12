# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import kamera.models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bilde',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bilde_nos', models.CharField(unique=True, max_length=20)),
                ('bilde_bilde', models.ImageField(null=True, upload_to=kamera.models.image_file_path, blank=True)),
                ('bilde_thumb', models.ImageField(null=True, upload_to=kamera.models.thumb_file_path, blank=True)),
                ('bilde_datums', models.DateTimeField(default=django.utils.timezone.now)),
                ('bilde_visible', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'bildes',
            },
        ),
        migrations.CreateModel(
            name='Kamera',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kamera_nos', models.CharField(max_length=100)),
                ('kamera_slug', models.SlugField(unique=True)),
                ('kamera_apraksts', models.TextField(default=b'kameras apraksts')),
                ('kamera_img_dir', models.CharField(default=b'username', max_length=50)),
                ('kamera_email', models.CharField(max_length=30, blank=True)),
            ],
            options={
                'db_table': 'kameras',
            },
        ),
    ]
