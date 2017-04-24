# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patrimonio', '0003_auto_20170422_1948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patrimonio',
            name='p_foto',
        ),
        migrations.AddField(
            model_name='patrimonio',
            name='p_imagem',
            field=models.CharField(default='null', max_length=100, verbose_name=b'Imagem'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patrimonio',
            name='p_ativo',
            field=models.BooleanField(default=False, verbose_name=b'Ativo'),
        ),
        migrations.AlterField(
            model_name='patrimonio',
            name='p_codigo',
            field=models.IntegerField(unique=True, verbose_name=b'C\xc3\xb3digo'),
        ),
        migrations.AlterField(
            model_name='patrimonio',
            name='p_data_att',
            field=models.DateField(verbose_name=b'Data atualizado'),
        ),
        migrations.AlterField(
            model_name='patrimonio',
            name='p_data_entrada',
            field=models.DateField(verbose_name=b'Data registro'),
        ),
        migrations.AlterField(
            model_name='patrimonio',
            name='p_data_saida',
            field=models.DateField(null=True, verbose_name=b'Data desativado'),
        ),
        migrations.AlterField(
            model_name='patrimonio',
            name='p_descricao',
            field=models.CharField(max_length=100, verbose_name=b'Descric\xc3\xa3o'),
        ),
        migrations.AlterField(
            model_name='patrimonio',
            name='p_estado',
            field=models.ForeignKey(verbose_name=b'Estado', to='patrimonio.Estado'),
        ),
        migrations.AlterField(
            model_name='patrimonio',
            name='p_id',
            field=models.AutoField(serialize=False, verbose_name=b'ID', primary_key=True),
        ),
        migrations.AlterField(
            model_name='patrimonio',
            name='p_obs',
            field=models.CharField(max_length=200, verbose_name=b'Observa\xc3\xa7\xc3\xa3o'),
        ),
        migrations.AlterField(
            model_name='patrimonio',
            name='p_responsavel',
            field=models.ForeignKey(verbose_name=b'Respons\xc3\xa1vel', to='patrimonio.Responsavel'),
        ),
    ]
