# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0002_groups_elder'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Groups',
            new_name='Group',
        ),
    ]
