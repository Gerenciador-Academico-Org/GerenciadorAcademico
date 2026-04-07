from django.contrib import admin
from .models import Professor, Sala, Disciplina, Aluno, Turma

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'capacidade')

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'professor')

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula')

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('disciplina', 'periodo')
    filter_horizontal = ('alunos',)