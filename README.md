# 🎓 Gerenciador Acadêmico

> **IFB - Bolsa Futuro Digital | Projeto Integrador de Desenvolvimento de Software**

Uma API RESTful robusta e inteligente para a gestão de grades horárias acadêmicas. O sistema foi projetado para organizar o corpo docente e a infraestrutura, garantindo a integridade da alocação de salas e professores de forma automatizada.

## ✨ Funcionalidades em Destaque
* 🔐 **Segurança Avançada:** Autenticação de usuários via tokens JWT (JSON Web Tokens).
* 🏛️ **Gestão Estrutural:** Controle relacional de Cursos, Turmas, Disciplinas e Salas físicas.
* 🧠 **Validação Inteligente (Anti-Conflito):** Algoritmo nativo que impede o agendamento de um professor em duas turmas simultâneas ou a sobreposição de aulas na mesma sala.
* ⚙️ **Painel Administrativo:** Interface Django Admin customizada para a gestão rápida de dados.

## 🚀 Roadmap e Entregas (Sprints)
- [x] **Sprint 1 & 2:** Setup Django, Custom User Model e Autenticação JWT.
- [x] **Sprint 3 & 4:** Gestão de Cursos, Turmas, Disciplinas e Salas.
- [x] **Sprint 5:** Estrutura da Matriz Semanal (Modelagem de Aulas).
- [x] **Sprint 6:** Lógica de Validação de Conflitos de Horários e Infraestrutura.
- [x] **Sprint 7:** Garantia de Qualidade Automatizada (Testes Unitários).

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.13
* **Framework:** Django 6.0.3 & Django REST Framework (DRF)
* **Autenticação:** djangorestframework-simplejwt
* **Banco de Dados:** SQLite (Ambiente de Desenvolvimento)

## 💻 Como executar o projeto localmente

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/Gerenciador-Academico-Org/GerenciadorAcademico.git](https://github.com/Gerenciador-Academico-Org/GerenciadorAcademico.git)
   cd GerenciadorAcademico
Ative o ambiente virtual:

Bash
.\venv\Scripts\activate
Instale as dependências:

Bash
pip install -r requirements.txt
Sincronize o banco de dados:

Bash
python manage.py makemigrations
python manage.py migrate
Inicie o servidor:

Bash
python manage.py runserver
✒️ Desenvolvido com rigor técnico por Cleber Moreira da Rocha e Equipe.
