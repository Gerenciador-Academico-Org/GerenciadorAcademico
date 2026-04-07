from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.nome

class Sala(models.Model):
    nome = models.CharField(max_length=50)
    capacidade = models.IntegerField()
    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome

# ESTAS SÃO AS CLASSES QUE O ERRO DISSE QUE NÃO ACHOU:
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    matricula = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.nome

class Turma(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, on_delete=models.SET_NULL, null=True)
    alunos = models.ManyToManyField(Aluno)
    periodo = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.disciplina.nome} ({self.periodo})"