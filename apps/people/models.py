from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Definindo os papéis conforme o plano de desenvolvimento
    ROLES = (
        ('coordenador_geral', 'Coordenador Geral'),
        ('coordenador_curso', 'Coordenador de Curso'),
        ('professor', 'Professor'),
    )

    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    papel = models.CharField(max_length=20, choices=ROLES, default='professor')
    ativo = models.BooleanField(default=True)
    ultimo_acesso = models.DateTimeField(auto_now=True)

    # Definindo o email como campo de login
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name']

    def __str__(self):
        return f"{self.first_name} ({self.get_papel_display()})"

# Modelo para vincular Coordenadores/Professores aos seus cursos
class VinculoUsuarioCurso(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    # O campo 'curso_id' será um Integer temporário até criarmos o app 'courses'
    curso_id = models.IntegerField()

    class Meta:
        verbose_name = "Vínculo Usuário-Curso"