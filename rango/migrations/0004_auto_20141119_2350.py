# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_auto_20141119_2317'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='cat_likes',
            new_name='likes',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='cat_views',
            new_name='views',
        ),
    ]
