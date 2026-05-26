from django.contrib import admin
from .models import (
    Perfil,
    Curso,
    VinculoUsuarioCurso,
    Turma,
    Disciplina,
    Professor,
    Sala,
    Aula,
    Prazo,
    Solicitacao,
    HistoricoAlteracao,
)


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ("usuario", "papel", "telefone", "ativo")
    list_filter = ("papel", "ativo")
    search_fields = (
        "usuario__username",
        "usuario__first_name",
        "usuario__last_name",
        "usuario__email",
    )


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("nome", "coordenador_responsavel", "turnos_oferecidos", "ativo")
    search_fields = ("nome",)
    list_filter = ("ativo",)


@admin.register(VinculoUsuarioCurso)
class VinculoUsuarioCursoAdmin(admin.ModelAdmin):
    list_display = ("usuario", "curso")
    list_filter = ("curso",)
    search_fields = (
        "usuario__username",
        "usuario__first_name",
        "usuario__last_name",
        "curso__nome",
    )


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ("nome", "curso", "turno", "numero_alunos", "periodo_letivo", "ativo")
    search_fields = ("nome", "curso__nome", "periodo_letivo")
    list_filter = ("curso", "turno", "ativo")


@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ("nome", "curso", "carga_horaria", "tipo", "ativo")
    search_fields = ("nome", "curso__nome")
    list_filter = ("curso", "tipo", "ativo")


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ("nome_completo", "especializacao", "ativo")
    search_fields = (
        "usuario__first_name",
        "usuario__last_name",
        "usuario__username",
        "usuario__email",
        "especializacao",
    )
    list_filter = ("ativo",)

    def nome_completo(self, obj):
        nome = obj.usuario.get_full_name()
        return nome if nome else obj.usuario.username

    nome_completo.short_description = "Professor"


@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ("nome_codigo", "bloco", "capacidade", "tipo", "ativo")
    search_fields = ("nome_codigo", "bloco", "tipo")
    list_filter = ("tipo", "ativo")


@admin.register(Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = (
        "disciplina",
        "turma",
        "professor",
        "sala",
        "dia_semana",
        "horario_inicio",
        "horario_fim",
        "periodo_letivo",
        "ano",
    )
    search_fields = (
        "disciplina__nome",
        "turma__nome",
        "professor__usuario__first_name",
        "professor__usuario__last_name",
        "professor__usuario__username",
        "sala__nome_codigo",
    )
    list_filter = ("dia_semana", "periodo_letivo", "ano", "sala")


@admin.register(Prazo)
class PrazoAdmin(admin.ModelAdmin):
    list_display = (
        "periodo_letivo",
        "ano",
        "data_inicio_ajustes_coordenadores",
        "data_fim_ajustes_coordenadores",
        "data_inicio_solicitacoes_professores",
        "data_fim_solicitacoes_professores",
    )
    search_fields = ("periodo_letivo",)
    list_filter = ("ano", "periodo_letivo")


@admin.register(Solicitacao)
class SolicitacaoAdmin(admin.ModelAdmin):
    list_display = ("tipo", "status", "remetente", "destinatario", "aula", "criado_em")
    search_fields = (
        "tipo",
        "descricao",
        "remetente__username",
        "remetente__first_name",
        "remetente__last_name",
        "destinatario__username",
    )
    list_filter = ("status", "tipo", "criado_em")


@admin.register(HistoricoAlteracao)
class HistoricoAlteracaoAdmin(admin.ModelAdmin):
    list_display = ("usuario", "data_hora", "acao", "tabela_afetada", "registro_id")
    search_fields = ("acao", "tabela_afetada", "usuario__username")
    list_filter = ("acao", "tabela_afetada", "data_hora")