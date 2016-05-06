# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='close_at',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='mark',
            name='open_at',
            field=models.TimeField(),
        ),
    ]
