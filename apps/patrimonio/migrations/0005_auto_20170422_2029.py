# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patrimonio', '0004_auto_20170422_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estado',
            name='e_descricao',
            field=models.CharField(max_length=100, verbose_name=b'Descri\xc3\xa7\xc3\xa3o'),
        ),
        migrations.AlterField(
            model_name='estado',
            name='e_id',
            field=models.AutoField(serialize=False, verbose_name=b'ID', primary_key=True),
        ),
        migrations.AlterField(
            model_name='localidade',
            name='l_descricao',
            field=models.CharField(max_length=100, verbose_name=b'Descri\xc3\xa7\xc3\xa3o'),
        ),
        migrations.AlterField(
            model_name='localidade',
            name='l_id',
            field=models.AutoField(serialize=False, verbose_name=b'ID', primary_key=True),
        ),
        migrations.AlterField(
            model_name='localidade',
            name='l_numero',
            field=models.IntegerField(verbose_name=b'N\xc3\xbamero'),
        ),
        migrations.AlterField(
            model_name='patrimonio',
            name='p_ativo',
            field=models.CharField(max_length=50, verbose_name=b'Ativo', choices=[(b'ativo', b'Ativo'), (b'inativo', b'Inativo')]),
        ),
        migrations.AlterField(
            model_name='responsavel',
            name='r_email',
            field=models.CharField(max_length=50, verbose_name=b'Email'),
        ),
        migrations.AlterField(
            model_name='responsavel',
            name='r_id',
            field=models.AutoField(serialize=False, verbose_name=b'ID', primary_key=True),
        ),
        migrations.AlterField(
            model_name='responsavel',
            name='r_local',
            field=models.ForeignKey(verbose_name=b'Local', to='patrimonio.Localidade'),
        ),
        migrations.AlterField(
            model_name='responsavel',
            name='r_nome',
            field=models.CharField(max_length=50, verbose_name=b'Nome'),
        ),
        migrations.AlterField(
            model_name='responsavel',
            name='r_tipo',
            field=models.CharField(max_length=50, verbose_name=b'Tipo', choices=[(b'morador', b'Morador'), (b'nao_morador', b'N\xc3\xa3o Morador')]),
        ),
    ]
