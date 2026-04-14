from django.test import TestCase
from django.core.exceptions import ValidationError
from datetime import time
from django.contrib.auth import get_user_model
from apps.schedule.models import Aula
from apps.rooms.models import Sala

User = get_user_model()

class AulaTestCase(TestCase):
    def setUp(self):
        """
        Fase de Instrução: Prepara o banco de dados temporário 
        criando os 'atores' necessários antes de cada teste.
        """
        self.professor_cleber = User.objects.create_user(username="prof_cleber", is_staff=True)
        
        # Sala principal para o teste, usando os campos corretos do seu models.py
        self.sala_juri = Sala.objects.create(
            nome_codigo="JURI-01", 
            bloco="Bloco A", 
            capacidade=50, 
            tipo="auditorio"
        )
        
        # Registra a primeira aula válida no banco de testes
        self.aula_matriz = Aula.objects.create(
            disciplina="Direito Civil",
            turma="DIR-2026",
            professor=self.professor_cleber,
            sala=self.sala_juri,
            dia_semana='SEG',
            horario_inicio=time(19, 0),
            horario_fim=time(21, 0)
        )

    def test_conflito_professor(self):
        """Testa se o sistema barra o mesmo professor em duas turmas no mesmo horário."""
        # Criação de uma segunda sala com os campos corretos
        sala_comum = Sala.objects.create(
            nome_codigo="SALA-101", 
            bloco="Bloco B", 
            capacidade=30, 
            tipo="comum"
        )
        
        aula_ilegal = Aula(
            disciplina="Direito Penal",
            turma="DIR-2027",
            professor=self.professor_cleber, # O mesmo professor
            sala=sala_comum,                 # Em uma sala diferente
            dia_semana='SEG',
            horario_inicio=time(19, 30),     # Horário sobreposto!
            horario_fim=time(22, 0)
        )
        
        # O teste PASSA se o sistema disparar o erro de validação
        with self.assertRaises(ValidationError):
            aula_ilegal.full_clean()

    def test_conflito_sala(self):
        """Testa se o sistema barra professores diferentes tentando usar a mesma sala."""
        professor_convidado = User.objects.create_user(username="prof_convidado", is_staff=True)
        
        aula_ilegal = Aula(
            disciplina="Direito Constitucional",
            turma="DIR-2028",
            professor=professor_convidado, # Professor diferente
            sala=self.sala_juri,           # Na mesma sala já ocupada!
            dia_semana='SEG',
            horario_inicio=time(18, 0),
            horario_fim=time(20, 0)        # Horário sobreposto!
        )
        
        # O teste PASSA se o sistema disparar o erro de validação
        with self.assertRaises(ValidationError):
            aula_ilegal.full_clean()