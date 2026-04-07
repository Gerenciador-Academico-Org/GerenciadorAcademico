from django.db import models
from apps.people.models import User

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    coordenador_responsavel = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, limit_choices_to={'papel': 'coordenador_curso'}
    )
    turnos_oferecidos = models.JSONField(default=list)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Turma(models.Model):
    TURNOS = (('matutino', 'Matutino'), ('vespertino', 'Vespertino'), ('noturno', 'Noturno'))
    nome = models.CharField(max_length=50)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='turmas')
    turno = models.CharField(max_length=20, choices=TURNOS)
    numero_alunos = models.PositiveIntegerField()
    periodo_letivo = models.CharField(max_length=10)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} - {self.curso.nome}"

class Disciplina(models.Model):
    TIPOS = (('teorica', 'Teórica'), ('pratica', 'Prática'))
    nome = models.CharField(max_length=100)
    carga_horaria = models.PositiveIntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='disciplinas')
    tipo = models.CharField(max_length=10, choices=TIPOS)
    ativo = models.BooleanField(default=True)
    professores = models.ManyToManyField(User, related_name='disciplinas_lecionadas', limit_choices_to={'papel': 'professor'})

    def __str__(self):
        return self.nome