from django.test import TestCase
from apps.rooms.models import Sala

class SalaTestCase(TestCase):
    def setUp(self):
        """
        Fase de Instrução: Cria uma sala padrão no banco de dados temporário
        para ser usada nas verificações abaixo.
        """
        self.sala_teste = Sala.objects.create(
            nome_codigo="LAB-TI",
            bloco="Bloco C",
            capacidade=30,
            tipo="laboratorio"
        )

    def test_sala_criada_com_sucesso(self):
        """
        Testa se o banco de dados está gravando e recuperando 
        as informações de infraestrutura corretamente.
        """
        # Busca a sala no banco de dados simulado
        sala_salva = Sala.objects.get(nome_codigo="LAB-TI")
        
        # Verifica se os dados batem com o que foi cadastrado
        self.assertEqual(sala_salva.bloco, "Bloco C")
        self.assertEqual(sala_salva.capacidade, 30)
        self.assertEqual(sala_salva.tipo, "laboratorio")

    def test_capacidade_sala(self):
        """Testa se o valor numérico da capacidade está correto."""
        self.assertTrue(self.sala_teste.capacidade > 0)