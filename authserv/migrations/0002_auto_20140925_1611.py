# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from uuid import uuid4


class Migration(migrations.Migration):

    dependencies = [
        ('authserv', '0001_initial'),
    ]

    operations = [
        migrations.AddField("User", "uuid", models.CharField(default="unresolved-uuid", max_length=45))

    ]
