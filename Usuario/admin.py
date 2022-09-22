from django.contrib import admin

from .import models

@admin.register(models.Usuario)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome','email', 'telefone', 'senha',)

@admin.register(models.Financa)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'tipo', 'descricao','valor')

