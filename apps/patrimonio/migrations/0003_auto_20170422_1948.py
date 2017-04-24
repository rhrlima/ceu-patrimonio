# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patrimonio', '0002_auto_20170420_2049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='u_responsavel',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
