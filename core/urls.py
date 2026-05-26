from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, PerfilViewSet, CursoViewSet, VinculoUsuarioCursoViewSet,
    TurmaViewSet, DisciplinaViewSet, ProfessorViewSet, SalaViewSet, AulaViewSet,
    PrazoViewSet, SolicitacaoViewSet, HistoricoAlteracaoViewSet,
    dashboard_api, disciplinas_nao_alocadas, verificar_conflito, sugerir_grade,
)

router = DefaultRouter()
router.register('usuarios', UserViewSet)
router.register('perfis', PerfilViewSet)
router.register('cursos', CursoViewSet)
router.register('vinculos', VinculoUsuarioCursoViewSet)
router.register('turmas', TurmaViewSet)
router.register('disciplinas', DisciplinaViewSet)
router.register('professores', ProfessorViewSet)
router.register('salas', SalaViewSet)
router.register('aulas', AulaViewSet)
router.register('prazos', PrazoViewSet)
router.register('solicitacoes', SolicitacaoViewSet)
router.register('historico', HistoricoAlteracaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('dashboard/', dashboard_api),
    path('disciplinas-nao-alocadas/', disciplinas_nao_alocadas),
    path('verificar-conflito/', verificar_conflito),
    path('sugerir-grade/', sugerir_grade),
]
