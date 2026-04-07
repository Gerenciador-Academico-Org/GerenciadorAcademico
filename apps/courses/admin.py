from django.contrib import admin
from .models import Curso, Turma, Disciplina

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'coordenador_responsavel', 'ativo')
    list_filter = ('ativo',)

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'curso', 'turno', 'periodo_letivo')
    list_filter = ('curso', 'turno')

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'curso', 'carga_horaria', 'tipo')
    list_filter = ('curso', 'tipo')