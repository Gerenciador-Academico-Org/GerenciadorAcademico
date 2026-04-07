from django.db import models
from django.core.exceptions import ValidationError

class Aula(models.Model):
    # Relacionamentos (Certifique-se que esses modelos existem nos outros apps)
    disciplina = models.CharField(max_length=100) # Ou ForeignKey para apps.courses.Disciplina
    turma = models.CharField(max_length=50)      # Ou ForeignKey para apps.courses.Turma
    professor = models.ForeignKey('people.User', on_delete=models.CASCADE) 
    sala = models.ForeignKey('rooms.Sala', on_delete=models.CASCADE)
    
    # Detalhes do Horário
    DIAS_CHOICES = [
        ('SEG', 'Segunda-feira'),
        ('TER', 'Terça-feira'),
        ('QUA', 'Quarta-feira'),
        ('QUI', 'Quinta-feira'),
        ('SEX', 'Sexta-feira'),
        ('SAB', 'Sábado'),
    ]
    dia_semana = models.CharField(max_length=3, choices=DIAS_CHOICES)
    horario_inicio = models.TimeField()
    horario_fim = models.TimeField()
    periodo_letivo = models.CharField(max_length=20, default="2026.1")

    def __str__(self):
        return f"{self.disciplina} - {self.turma} ({self.dia_semana})"

    def clean(self):
        # Lógica de conflito (Sprint 6)
        conflitos = Aula.objects.filter(
            dia_semana=self.dia_semana,
            horario_inicio__lt=self.horario_fim,
            horario_fim__gt=self.horario_inicio
        ).exclude(pk=self.pk)

        if conflitos.filter(professor=self.professor).exists():
            raise ValidationError("O professor já tem aula nesse horário!")
        
        if conflitos.filter(sala=self.sala).exists():
            raise ValidationError("Esta sala já está ocupada nesse horário!")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)