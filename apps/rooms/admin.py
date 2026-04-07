from django.contrib import admin
from .models import Sala

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ('nome_codigo', 'bloco', 'capacidade', 'tipo', 'ativo')
    list_filter = ('bloco', 'tipo', 'ativo')