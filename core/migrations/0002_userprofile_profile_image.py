# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(upload_to='/media/', blank=True, null=True),
            preserve_default=True,
        ),
    ]
