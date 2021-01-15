# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kamera', '0048_auto_20200117_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kamera',
            name='kamera_ai',
            field=models.BooleanField(default=False, verbose_name=b'b\xc4\x93rns?'),
        ),
        migrations.AlterField(
            model_name='kamera',
            name='kamera_apraksts',
            field=models.TextField(default=b'', null=True, verbose_name=b'alt teksts', blank=True),
        ),
        migrations.AlterField(
            model_name='kamera',
            name='kamera_email',
            field=models.CharField(max_length=30, verbose_name=b'e-pasts@kuvalda.lv', blank=True),
        ),
        migrations.AlterField(
            model_name='kamera',
            name='kamera_ftp',
            field=models.BooleanField(default=False, verbose_name=b'FTP?'),
        ),
        migrations.AlterField(
            model_name='kamera',
            name='kamera_img_dir',
            field=models.CharField(default=b'username', max_length=50, verbose_name=b'sist\xc4\x93mas mape'),
        ),
        migrations.AlterField(
            model_name='kamera',
            name='kamera_nos',
            field=models.CharField(max_length=100, verbose_name=b'nosaukums'),
        ),
        migrations.AlterField(
            model_name='kamera',
            name='kamera_slug',
            field=models.SlugField(default=b'57f19b1064b5', unique=True, verbose_name=b'url nosaukums'),
        ),
        migrations.AlterField(
            model_name='kamera',
            name='kamera_type',
            field=models.CharField(default=b'PUB', max_length=10, verbose_name=b'tips', choices=[(b'PUB', b'public'), (b'PRIV', b'private'), (b'SEC', b'security')]),
        ),
    ]
