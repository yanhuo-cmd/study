# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areainfo',
            name='aParent',
            field=models.ForeignKey(blank=True, to='booktest.AreaInfo', null=True),
        ),
    ]
