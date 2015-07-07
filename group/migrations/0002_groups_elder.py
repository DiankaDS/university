# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='groups',
            name='elder',
            field=models.OneToOneField(to='student.Students', null=True, related_name='elder', blank=True),
            preserve_default=True,
        ),
    ]
