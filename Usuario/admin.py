from django.contrib import admin

from Usuario.models import Usuario

@admin.register(Usuario)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome','email', 'telefone', 'senha',)
