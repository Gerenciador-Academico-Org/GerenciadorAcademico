from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Perfil(models.Model):
    PAPEIS = [
        ('coordenador_geral', 'Coordenador Geral'),
        ('coordenador_curso', 'Coordenador de Curso'),
        ('professor', 'Professor'),
    ]
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    papel = models.CharField(max_length=30, choices=PAPEIS, default='professor')
    telefone = models.CharField(max_length=30, blank=True)
    ativo = models.BooleanField(default=True)
    ultimo_acesso = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.usuario.get_full_name() or self.usuario.username} - {self.get_papel_display()}'


class Curso(models.Model):
    nome = models.CharField(max_length=120, unique=True)
    coordenador_responsavel = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    turnos_oferecidos = models.CharField(max_length=120, default='Matutino, Vespertino, Noturno')
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class VinculoUsuarioCurso(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('usuario', 'curso')
        verbose_name = 'Vínculo usuário/curso'
        verbose_name_plural = 'Vínculos usuários/cursos'

    def __str__(self):
        return f'{self.usuario.username} -> {self.curso.nome}'


class Turma(models.Model):
    TURNOS = [('matutino', 'Matutino'), ('vespertino', 'Vespertino'), ('noturno', 'Noturno')]
    nome = models.CharField(max_length=120)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='turmas')
    turno = models.CharField(max_length=20, choices=TURNOS)
    numero_alunos = models.PositiveIntegerField(default=0)
    periodo_letivo = models.CharField(max_length=20, default='2026.1')
    ativo = models.BooleanField(default=True)

    class Meta:
        unique_together = ('nome', 'curso', 'periodo_letivo')

    def __str__(self):
        return f'{self.nome} - {self.curso.nome}'


class Disciplina(models.Model):
    TIPOS = [('teorica', 'Teórica'), ('pratica', 'Prática')]
    nome = models.CharField(max_length=120)
    carga_horaria = models.PositiveIntegerField(default=60)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='disciplinas')
    tipo = models.CharField(max_length=20, choices=TIPOS, default='teorica')
    professores = models.ManyToManyField(User, blank=True, related_name='disciplinas_habilitadas')
    ativo = models.BooleanField(default=True)

    class Meta:
        unique_together = ('nome', 'curso')

    def __str__(self):
        return self.nome


class Professor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='professor')
    especializacao = models.CharField(max_length=150, blank=True)
    disponibilidade = models.JSONField(default=dict, blank=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.usuario.get_full_name() or self.usuario.username


class Sala(models.Model):
    TIPOS = [('comum', 'Comum'), ('laboratorio', 'Laboratório'), ('auditorio', 'Auditório')]
    nome_codigo = models.CharField(max_length=60, unique=True)
    bloco = models.CharField(max_length=80, blank=True)
    capacidade = models.PositiveIntegerField(default=30)
    tipo = models.CharField(max_length=30, choices=TIPOS, default='comum')
    recursos_disponiveis = models.CharField(max_length=255, blank=True, help_text='Ex.: Projetor, Ar-condicionado, Quadro')
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nome_codigo} ({self.capacidade} lugares)'


class Aula(models.Model):
    DIAS = [
        ('segunda', 'Segunda'), ('terca', 'Terça'), ('quarta', 'Quarta'),
        ('quinta', 'Quinta'), ('sexta', 'Sexta'), ('sabado', 'Sábado'),
    ]
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='aulas')
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='aulas')
    professor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='aulas_ministradas')
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, related_name='aulas')
    dia_semana = models.CharField(max_length=20, choices=DIAS)
    horario_inicio = models.TimeField()
    horario_fim = models.TimeField()
    periodo_letivo = models.CharField(max_length=20, default='2026.1')
    ano = models.PositiveIntegerField(default=2026)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['dia_semana', 'horario_inicio']

    def __str__(self):
        return f'{self.disciplina} | {self.turma} | {self.dia_semana} {self.horario_inicio}-{self.horario_fim}'

    def clean(self):
        if self.horario_inicio >= self.horario_fim:
            raise ValidationError('Horário inicial deve ser menor que o horário final.')
        conflitos_professor = Aula.objects.filter(
            professor=self.professor, dia_semana=self.dia_semana,
            horario_inicio__lt=self.horario_fim, horario_fim__gt=self.horario_inicio,
            periodo_letivo=self.periodo_letivo,
        ).exclude(pk=self.pk)
        if conflitos_professor.exists():
            raise ValidationError('Conflito: professor já ocupado nesse horário.')
        conflitos_sala = Aula.objects.filter(
            sala=self.sala, dia_semana=self.dia_semana,
            horario_inicio__lt=self.horario_fim, horario_fim__gt=self.horario_inicio,
            periodo_letivo=self.periodo_letivo,
        ).exclude(pk=self.pk)
        if conflitos_sala.exists():
            raise ValidationError('Conflito: sala já ocupada nesse horário.')
        conflitos_turma = Aula.objects.filter(
            turma=self.turma, dia_semana=self.dia_semana,
            horario_inicio__lt=self.horario_fim, horario_fim__gt=self.horario_inicio,
            periodo_letivo=self.periodo_letivo,
        ).exclude(pk=self.pk)
        if conflitos_turma.exists():
            raise ValidationError('Conflito: turma já possui aula nesse horário.')
        if self.sala and self.turma and self.sala.capacidade < self.turma.numero_alunos:
            raise ValidationError('Capacidade insuficiente: sala menor que a quantidade de alunos da turma.')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class Prazo(models.Model):
    ano = models.PositiveIntegerField(default=2026)
    periodo_letivo = models.CharField(max_length=20, default='2026.1')
    data_inicio_ajustes_coordenadores = models.DateField()
    data_fim_ajustes_coordenadores = models.DateField()
    data_inicio_solicitacoes_professores = models.DateField()
    data_fim_solicitacoes_professores = models.DateField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f'Prazos {self.periodo_letivo}'


class Solicitacao(models.Model):
    TIPOS = [('ajuste_coordenador', 'Ajuste do Coordenador'), ('troca_professor', 'Troca solicitada pelo Professor')]
    STATUS = [('pendente', 'Pendente'), ('aprovada_coord', 'Aprovada pelo Coordenador'), ('aprovada', 'Aprovada Final'), ('rejeitada', 'Rejeitada')]
    tipo = models.CharField(max_length=40, choices=TIPOS)
    descricao = models.TextField()
    status = models.CharField(max_length=30, choices=STATUS, default='pendente')
    remetente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solicitacoes_enviadas')
    destinatario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='solicitacoes_recebidas')
    aula = models.ForeignKey(Aula, on_delete=models.SET_NULL, null=True, blank=True)
    dados_sugeridos = models.JSONField(default=dict, blank=True)
    motivo_resposta = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.get_tipo_display()} - {self.get_status_display()}'


class HistoricoAlteracao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    data_hora = models.DateTimeField(default=timezone.now)
    acao = models.CharField(max_length=30)
    tabela_afetada = models.CharField(max_length=80)
    registro_id = models.CharField(max_length=80)
    dados_anteriores = models.JSONField(default=dict, blank=True)
    dados_novos = models.JSONField(default=dict, blank=True)

    class Meta:
        ordering = ['-data_hora']
        verbose_name = 'Histórico de alteração'
        verbose_name_plural = 'Histórico de alterações'

    def __str__(self):
        return f'{self.acao} em {self.tabela_afetada} #{self.registro_id}'
