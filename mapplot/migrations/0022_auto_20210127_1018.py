# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapplot', '0021_auto_20210127_0426'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mapplot',
            options={'verbose_name_plural': 'Punkti'},
        ),
        migrations.AlterModelOptions(
            name='mapplotcity',
            options={'verbose_name_plural': 'Pils\u0113tas'},
        ),
        migrations.AlterModelOptions(
            name='mapplotimage',
            options={'verbose_name_plural': 'Punktu att\u0113li'},
        ),
        migrations.AlterModelOptions(
            name='mapplottype',
            options={'verbose_name_plural': 'Punktu tipi'},
        ),
        migrations.AlterModelOptions(
            name='mapplotusercity',
            options={'verbose_name_plural': 'Lietot\u0101ji <--> Pils\u0113tas'},
        ),
    ]
