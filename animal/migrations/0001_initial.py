# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kamera', '0041_auto_20191218_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalCoords',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('x1', models.IntegerField(default=0)),
                ('y1', models.IntegerField(default=0)),
                ('x2', models.IntegerField(default=0)),
                ('y2', models.IntegerField(default=0)),
                ('a_img', models.ForeignKey(blank=True, to='kamera.Bilde', null=True)),
            ],
            options={
                'db_table': 'animal_coords',
            },
        ),
        migrations.CreateModel(
            name='AnimalType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('a_type', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'animal_type',
            },
        ),
        migrations.AddField(
            model_name='animalcoords',
            name='a_type',
            field=models.ForeignKey(default=1, to='animal.AnimalType'),
        ),
    ]
