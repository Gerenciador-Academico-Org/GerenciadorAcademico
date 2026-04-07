# 🎓 Gerenciador Acadêmico - IFB Bolsa Futuro Digital

Sistema inteligente para gestão de grade horária acadêmica, desenvolvido como projeto prático para o curso de Desenvolvimento de Software.

## 🚀 Status do Projeto: Sprint 6 em andamento
- [x] **Sprint 1 & 2**: Setup Django, Custom User Model e Autenticação JWT.
- [x] **Sprint 3 & 4**: Gestão de Cursos, Turmas, Disciplinas e Salas.
- [x] **Sprint 5**: Estrutura da Matriz Semanal (Matriz de Aulas).
- [ ] **Sprint 6**: Lógica de Validação de Conflitos (Em desenvolvimento).

## 🛠️ Tecnologias
- **Backend**: Django 6.0 + Django REST Framework.
- **Segurança**: SimpleJWT (Tokens de 7 dias).
- **Banco de Dados**: SQLite (Desenvolvimento).

## 💻 Como rodar o projeto
1. Clone o repositório: `git clone https://github.com/Gerenciador-Academico-Org/GerenciadorAcademico.git`
2. Ative a venv: `.\venv\Scripts\activate`
3. Instale as dependências: `pip install -r requirements.txt`
4. Rode as migrações: `python manage.py migrate`
5. Inicie o servidor: `python manage.py runserver`

---
*Desenvolvido por Cleber Moreira da Rocha e Equipe.*