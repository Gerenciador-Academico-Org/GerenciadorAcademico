from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Perfil, Curso, VinculoUsuarioCurso, Turma, Disciplina, Professor, Sala, Aula, Prazo, Solicitacao, HistoricoAlteracao
from .serializers import (
    UserSerializer, PerfilSerializer, CursoSerializer, VinculoUsuarioCursoSerializer,
    TurmaSerializer, DisciplinaSerializer, ProfessorSerializer, SalaSerializer,
    AulaSerializer, PrazoSerializer, SolicitacaoSerializer, HistoricoAlteracaoSerializer,
)


def home(request):
    contexto = {
        'cursos': Curso.objects.count(),
        'turmas': Turma.objects.count(),
        'disciplinas': Disciplina.objects.count(),
        'professores': Professor.objects.count(),
        'salas': Sala.objects.count(),
        'aulas': Aula.objects.count(),
        'solicitacoes': Solicitacao.objects.filter(status='pendente').count(),
    }
    return render(request, 'core/home.html', contexto)


def grade_visual(request):
    dias = ['segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado']
    horarios = sorted(set(Aula.objects.values_list('horario_inicio', flat=True)))
    aulas = Aula.objects.select_related('disciplina', 'turma', 'professor', 'sala').all()
    matriz = []
    for horario in horarios:
        linha = {'horario': horario, 'dias': []}
        for dia in dias:
            aula = aulas.filter(dia_semana=dia, horario_inicio=horario).first()
            linha['dias'].append(aula)
        matriz.append(linha)
    return render(request, 'core/grade.html', {'dias': dias, 'matriz': matriz})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer

class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.select_related('usuario').all()
    serializer_class = PerfilSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class VinculoUsuarioCursoViewSet(viewsets.ModelViewSet):
    queryset = VinculoUsuarioCurso.objects.select_related('usuario', 'curso').all()
    serializer_class = VinculoUsuarioCursoSerializer

class TurmaViewSet(viewsets.ModelViewSet):
    queryset = Turma.objects.select_related('curso').all()
    serializer_class = TurmaSerializer

class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.select_related('curso').prefetch_related('professores').all()
    serializer_class = DisciplinaSerializer

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.select_related('usuario').all()
    serializer_class = ProfessorSerializer

class SalaViewSet(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer

class AulaViewSet(viewsets.ModelViewSet):
    queryset = Aula.objects.select_related('disciplina', 'turma', 'professor', 'sala', 'turma__curso').all()
    serializer_class = AulaSerializer

class PrazoViewSet(viewsets.ModelViewSet):
    queryset = Prazo.objects.all()
    serializer_class = PrazoSerializer

class SolicitacaoViewSet(viewsets.ModelViewSet):
    queryset = Solicitacao.objects.select_related('remetente', 'destinatario', 'aula').all()
    serializer_class = SolicitacaoSerializer

class HistoricoAlteracaoViewSet(viewsets.ModelViewSet):
    queryset = HistoricoAlteracao.objects.select_related('usuario').all()
    serializer_class = HistoricoAlteracaoSerializer


@api_view(['GET'])
def dashboard_api(request):
    total_aulas = Aula.objects.count()
    total_disciplinas = Disciplina.objects.count()
    disciplinas_alocadas = Disciplina.objects.filter(aulas__isnull=False).distinct().count()
    pendentes = max(total_disciplinas - disciplinas_alocadas, 0)
    ocupacao_salas = Sala.objects.annotate(total_aulas=Count('aulas')).values('id', 'nome_codigo', 'capacidade', 'total_aulas')
    return Response({
        'resumo': {
            'usuarios': User.objects.count(),
            'cursos': Curso.objects.count(),
            'turmas': Turma.objects.count(),
            'disciplinas': total_disciplinas,
            'professores': Professor.objects.count(),
            'salas': Sala.objects.count(),
            'aulas_alocadas': total_aulas,
            'disciplinas_pendentes': pendentes,
            'solicitacoes_pendentes': Solicitacao.objects.filter(status='pendente').count(),
        },
        'ocupacao_salas': list(ocupacao_salas),
    })


@api_view(['GET'])
def disciplinas_nao_alocadas(request):
    qs = Disciplina.objects.filter(aulas__isnull=True).distinct()
    return Response(DisciplinaSerializer(qs, many=True).data)


@api_view(['POST'])
def verificar_conflito(request):
    serializer = AulaSerializer(data=request.data)
    if serializer.is_valid():
        return Response({'conflito': False, 'mensagem': 'Horário disponível.'})
    return Response({'conflito': True, 'erros': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def sugerir_grade(request):
    """Sugestão simples para apresentação: lista disciplinas sem aula e sugere a primeira sala/professor disponíveis."""
    sugestoes = []
    dias = ['segunda', 'terca', 'quarta', 'quinta', 'sexta']
    horarios = [('08:00', '09:40'), ('10:00', '11:40'), ('19:00', '20:40')]
    salas = list(Sala.objects.filter(ativo=True).order_by('-capacidade'))
    for disciplina in Disciplina.objects.filter(ativo=True, aulas__isnull=True).distinct():
        professor = disciplina.professores.first() or User.objects.filter(professor__isnull=False).first()
        turma = Turma.objects.filter(curso=disciplina.curso, ativo=True).first()
        if not professor or not turma or not salas:
            continue
        encontrado = None
        for dia in dias:
            for inicio, fim in horarios:
                for sala in salas:
                    dados = {
                        'disciplina': disciplina.id, 'turma': turma.id, 'professor': professor.id,
                        'sala': sala.id, 'dia_semana': dia, 'horario_inicio': inicio,
                        'horario_fim': fim, 'periodo_letivo': turma.periodo_letivo, 'ano': 2026,
                    }
                    s = AulaSerializer(data=dados)
                    if s.is_valid():
                        encontrado = dados
                        break
                if encontrado: break
            if encontrado: break
        if encontrado:
            sugestoes.append(encontrado)
    return Response({'total_sugestoes': len(sugestoes), 'sugestoes': sugestoes})
