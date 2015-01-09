# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authserv', '0002_auto_20140925_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.CharField(max_length=45),
        ),
    ]
