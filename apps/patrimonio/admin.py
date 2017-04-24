from django.contrib import admin
from apps.patrimonio.models import *


class EstadoAdmin(admin.ModelAdmin):
	model = Estado
	list_display = ['e_descricao']
	list_filter = []
	search_fields = ['e_descricao']
	save_on_top = True
admin.site.register(Estado, EstadoAdmin)


class LocalidadeAdmin(admin.ModelAdmin):
	model = Localidade
	list_display = ['l_numero', 'l_descricao']
	list_filter = []
	search_fields = ['l_descricao']
	save_on_top = True
admin.site.register(Localidade, LocalidadeAdmin)


class ResponsavelAdmin(admin.ModelAdmin):
	model = Responsavel
	list_display = ['r_nome', 'r_local', 'r_tipo']
	list_filter = ['r_tipo']
	search_fields = ['r_nome']
	save_on_top = True
admin.site.register(Responsavel, ResponsavelAdmin)


#admin.site.register(Usuario, admin.ModelAdmin)


class PatrimonioAdmin(admin.ModelAdmin):
	model = Patrimonio
	list_display = ['p_codigo', 'p_descricao', 'p_estado', 'p_responsavel', 'p_data_att', 'p_ativo']
	list_filter = ['p_ativo']
	search_fields = ['p_descricao']
	save_on_top = True
admin.site.register(Patrimonio, PatrimonioAdmin)