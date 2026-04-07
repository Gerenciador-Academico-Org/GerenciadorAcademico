from django.contrib import admin
from .models import Aula

@admin.register(Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = ('disciplina', 'turma', 'professor', 'sala', 'dia_semana', 'horario_inicio')
    list_filter = ('dia_semana', 'turma', 'professor')