from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Perfil, Curso, VinculoUsuarioCurso, Turma, Disciplina, Professor, Sala, Aula, Prazo, Solicitacao, HistoricoAlteracao

class UserSerializer(serializers.ModelSerializer):
    nome_completo = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'nome_completo']
    def get_nome_completo(self, obj):
        return obj.get_full_name() or obj.username

class PerfilSerializer(serializers.ModelSerializer):
    usuario_detalhe = UserSerializer(source='usuario', read_only=True)
    class Meta:
        model = Perfil
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class VinculoUsuarioCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VinculoUsuarioCurso
        fields = '__all__'

class TurmaSerializer(serializers.ModelSerializer):
    curso_nome = serializers.CharField(source='curso.nome', read_only=True)
    class Meta:
        model = Turma
        fields = '__all__'

class DisciplinaSerializer(serializers.ModelSerializer):
    curso_nome = serializers.CharField(source='curso.nome', read_only=True)
    class Meta:
        model = Disciplina
        fields = '__all__'

class ProfessorSerializer(serializers.ModelSerializer):
    nome = serializers.CharField(source='usuario.get_full_name', read_only=True)
    username = serializers.CharField(source='usuario.username', read_only=True)
    class Meta:
        model = Professor
        fields = '__all__'

class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = '__all__'

class AulaSerializer(serializers.ModelSerializer):
    disciplina_nome = serializers.CharField(source='disciplina.nome', read_only=True)
    turma_nome = serializers.CharField(source='turma.nome', read_only=True)
    professor_nome = serializers.SerializerMethodField()
    sala_nome = serializers.CharField(source='sala.nome_codigo', read_only=True)
    curso_nome = serializers.CharField(source='turma.curso.nome', read_only=True)
    class Meta:
        model = Aula
        fields = '__all__'
    def get_professor_nome(self, obj):
        return obj.professor.get_full_name() or obj.professor.username
    def validate(self, attrs):
        instance = Aula(**attrs)
        if self.instance:
            instance.pk = self.instance.pk
        instance.clean()
        return attrs

class PrazoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prazo
        fields = '__all__'

class SolicitacaoSerializer(serializers.ModelSerializer):
    remetente_nome = serializers.SerializerMethodField()
    class Meta:
        model = Solicitacao
        fields = '__all__'
    def get_remetente_nome(self, obj):
        return obj.remetente.get_full_name() or obj.remetente.username

class HistoricoAlteracaoSerializer(serializers.ModelSerializer):
    usuario_nome = serializers.SerializerMethodField()
    class Meta:
        model = HistoricoAlteracao
        fields = '__all__'
    def get_usuario_nome(self, obj):
        return obj.usuario.get_full_name() if obj.usuario else 'Sistema'
