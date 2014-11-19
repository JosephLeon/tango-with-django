# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20141119_2238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='likes',
            new_name='cat_likes',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='views',
            new_name='cat_views',
        ),
    ]
