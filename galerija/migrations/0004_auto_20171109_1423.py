# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galerija', '0003_auto_20170925_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalerijaKoment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('koment_text', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'galerija_koment',
            },
        ),
        migrations.AddField(
            model_name='galerija',
            name='bilde_like',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='galerijakoment',
            name='koment_bilde',
            field=models.ForeignKey(default=1, to='galerija.Galerija'),
        ),
    ]
