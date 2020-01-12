# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galerija', '0005_galerijakoment_koment_datums'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalerijaLike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bilde_plus', models.IntegerField(default=0)),
                ('bilde_minus', models.IntegerField(default=0)),
                ('bilde', models.ForeignKey(blank=True, to='galerija.Galerija', null=True)),
            ],
            options={
                'db_table': 'galerija_like',
            },
        ),
    ]
