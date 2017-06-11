# -*- coding: utf-8 -*-

from django.db import models

class Estado(models.Model):

	def __unicode__(self):
		return self.e_descricao

	e_id = models.AutoField(primary_key=True, verbose_name='ID')
	e_descricao = models.CharField(max_length=100, verbose_name='Descrição')


class Localidade(models.Model):

	def __unicode__(self):
		return self.l_descricao

	l_id = models.AutoField(primary_key=True, verbose_name='ID')
	l_numero = models.IntegerField(verbose_name='Número')
	l_descricao = models.CharField(max_length=100, verbose_name='Descrição')


class Responsavel(models.Model):

	class Meta:
		verbose_name_plural = "Responsáveis"

	def __unicode__(self):
		return self.r_nome

	TIPO_CHOICES = (
		('morador', 'Morador'),
		('nao_morador', 'Não Morador')
	)

	r_id = models.AutoField(primary_key=True, verbose_name='ID')
	r_nome = models.CharField(max_length=50, verbose_name='Nome')
	r_local = models.ForeignKey(Localidade, verbose_name='Local')
	r_email = models.CharField(max_length=50, verbose_name='Email')
	r_tipo = models.CharField(max_length=50, choices=TIPO_CHOICES, verbose_name='Tipo')


"""
class Usuario(models.Model):

	def __unicode__(self):
		return "Usuario: " + self.u_responsavel.r_nome

	u_id = models.AutoField(primary_key=True)
	u_responsavel = models.ForeignKey(Responsavel)
	u_login = models.CharField(max_length=20)
	u_grupo = models.CharField(max_length=30)
"""

class Patrimonio(models.Model):

	def __unicode__(self):
		return str(self.p_codigo) + " " + self.p_descricao

	ATIVO_CHOICES = (
		('ativo', 'Ativo'),
		('inativo', 'Inativo')
	)

	p_id = models.AutoField(primary_key=True, verbose_name='ID')
	p_codigo = models.IntegerField(unique=True, verbose_name='Código')
	p_descricao = models.CharField(max_length=100, verbose_name='Descricão')
	p_estado = models.ForeignKey(Estado, verbose_name='Estado')
	p_responsavel = models.ForeignKey(Responsavel, verbose_name='Responsável')
	p_data_entrada = models.DateField(verbose_name='Data registro')
	p_data_saida = models.DateField(blank=True, null=True, verbose_name='Data desativado')
	p_data_att = models.DateField(verbose_name='Data atualizado')
	p_imagem = models.CharField(max_length=100, verbose_name='Imagem')
	p_ativo = models.CharField(max_length=50, choices=ATIVO_CHOICES, verbose_name='Ativo')
	p_obs = models.CharField(max_length=200, verbose_name='Observação')