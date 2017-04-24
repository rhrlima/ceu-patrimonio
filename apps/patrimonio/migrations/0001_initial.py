# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('e_id', models.AutoField(serialize=False, primary_key=True)),
                ('e_descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Localidade',
            fields=[
                ('l_id', models.AutoField(serialize=False, primary_key=True)),
                ('l_numero', models.IntegerField()),
                ('l_descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Patrimonio',
            fields=[
                ('p_id', models.AutoField(serialize=False, primary_key=True)),
                ('p_codigo', models.IntegerField(unique=True)),
                ('p_descricao', models.CharField(max_length=100)),
                ('p_data_entrada', models.DateField()),
                ('p_data_saida', models.DateField()),
                ('p_data_att', models.DateField()),
                ('p_foto', models.CharField(max_length=100)),
                ('p_ativo', models.BooleanField()),
                ('p_obs', models.CharField(max_length=200)),
                ('p_estado', models.ForeignKey(to='patrimonio.Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Responsavel',
            fields=[
                ('m_id', models.AutoField(serialize=False, primary_key=True)),
                ('m_nome', models.CharField(max_length=50)),
                ('m_email', models.CharField(max_length=50)),
                ('m_tipo', models.BooleanField()),
                ('m_local', models.ForeignKey(to='patrimonio.Localidade')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('u_id', models.AutoField(serialize=False, primary_key=True)),
                ('u_login', models.CharField(max_length=20)),
                ('u_grupo', models.CharField(max_length=30)),
                ('u_responsavel', models.ForeignKey(to='patrimonio.Responsavel')),
            ],
        ),
        migrations.AddField(
            model_name='patrimonio',
            name='p_responsavel',
            field=models.ForeignKey(to='patrimonio.Responsavel'),
        ),
    ]
