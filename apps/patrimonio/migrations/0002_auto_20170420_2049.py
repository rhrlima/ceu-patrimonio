# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patrimonio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='responsavel',
            options={'verbose_name_plural': 'Responsaveis'},
        ),
        migrations.RenameField(
            model_name='responsavel',
            old_name='m_email',
            new_name='r_email',
        ),
        migrations.RenameField(
            model_name='responsavel',
            old_name='m_id',
            new_name='r_id',
        ),
        migrations.RenameField(
            model_name='responsavel',
            old_name='m_local',
            new_name='r_local',
        ),
        migrations.RenameField(
            model_name='responsavel',
            old_name='m_nome',
            new_name='r_nome',
        ),
        migrations.RenameField(
            model_name='responsavel',
            old_name='m_tipo',
            new_name='r_tipo',
        ),
    ]
