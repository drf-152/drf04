# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_bbbb_cccc'),
    ]

    operations = [
        migrations.AddField(
            model_name='aaaa',
            name='bbs',
            field=models.ManyToManyField(related_name='aa_bbs', null=True, to='core.BBBB', blank=True),
            preserve_default=True,
        ),
    ]
