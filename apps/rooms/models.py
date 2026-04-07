from django.db import models

class Sala(models.Model):
    TIPOS = (
        ('comum', 'Comum'),
        ('laboratorio', 'Laboratório'),
        ('auditorio', 'Auditório')
    )
    # nome_codigo deve ser único conforme o requisito da Sprint 4
    nome_codigo = models.CharField(max_length=20, unique=True)
    bloco = models.CharField(max_length=50)
    capacidade = models.PositiveIntegerField()
    tipo = models.CharField(max_length=20, choices=TIPOS)
    recursos_disponiveis = models.JSONField(default=list)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome_codigo} ({self.bloco})"