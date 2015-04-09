# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_aaaa_bbs'),
    ]

    operations = [
        migrations.AddField(
            model_name='cccc',
            name='show_me',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
