from django.contrib import admin
from .models import Perfil, Curso, VinculoUsuarioCurso, Turma, Disciplina, Professor, Sala, Aula, Prazo, Solicitacao, HistoricoAlteracao

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'papel', 'telefone', 'ativo')
    list_filter = ('papel', 'ativo')
    search_fields = ('usuario__username', 'usuario__first_name', 'usuario__last_name', 'usuario__email')

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'coordenador_responsavel', 'turnos_oferecidos', 'ativo')
    search_fields = ('nome',)
    list_filter = ('ativo',)

@admin.register(VinculoUsuarioCurso)
class VinculoUsuarioCursoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'curso')
    list_filter = ('curso',)

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'curso', 'turno', 'numero_alunos', 'periodo_letivo', 'ativo')
    list_filter = ('curso', 'turno', 'periodo_letivo', 'ativo')
    search_fields = ('nome',)

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'curso', 'carga_horaria', 'tipo', 'ativo')
    list_filter = ('curso', 'tipo', 'ativo')
    search_fields = ('nome',)
    filter_horizontal = ('professores',)

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'especializacao', 'ativo')
    search_fields = ('usuario__username', 'usuario__first_name', 'usuario__last_name')
    list_filter = ('ativo',)

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ('nome_codigo', 'bloco', 'capacidade', 'tipo', 'ativo')
    list_filter = ('tipo', 'bloco', 'ativo')
    search_fields = ('nome_codigo', 'bloco')

@admin.register(Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = ('disciplina', 'turma', 'professor', 'sala', 'dia_semana', 'horario_inicio', 'horario_fim', 'periodo_letivo')
    list_filter = ('dia_semana', 'periodo_letivo', 'sala', 'turma__curso')
    search_fields = ('disciplina__nome', 'turma__nome', 'professor__username', 'sala__nome_codigo')

@admin.register(Prazo)
class PrazoAdmin(admin.ModelAdmin):
    list_display = ('periodo_letivo', 'ano', 'ativo', 'data_inicio_ajustes_coordenadores', 'data_fim_ajustes_coordenadores')
    list_filter = ('ativo', 'ano', 'periodo_letivo')

@admin.register(Solicitacao)
class SolicitacaoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'status', 'remetente', 'destinatario', 'criado_em')
    list_filter = ('tipo', 'status')
    search_fields = ('descricao', 'remetente__username')

@admin.register(HistoricoAlteracao)
class HistoricoAlteracaoAdmin(admin.ModelAdmin):
    list_display = ('data_hora', 'usuario', 'acao', 'tabela_afetada', 'registro_id')
    list_filter = ('acao', 'tabela_afetada')
