# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animalcoords',
            name='a_type',
            field=models.ForeignKey(blank=True, to='animal.AnimalType', null=True),
        ),
    ]
