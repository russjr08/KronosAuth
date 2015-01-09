# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=10)),
                ('password_hash', models.CharField(max_length=100)),
                ('auth_token', models.CharField(max_length=80)),
            ],
            options={
            },
            bases=(models.Model,),
        ),

    ]
