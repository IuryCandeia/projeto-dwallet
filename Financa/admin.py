from django.contrib import admin

from Financa.models import Financa

@admin.register(Financa)
class FinancaAdmin(admin.ModelAdmin):
    list_display =  ('id', 'titulo', 'descricao', 'valor')
