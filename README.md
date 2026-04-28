# Sistema Inteligente de Gerenciamento de Salas e Horários Acadêmicos

## 📖 Sobre o Projeto
Projeto desenvolvido como parte do plano de trabalho "Residência em Desenvolvimento de Software - Bolsa Futuro Digital" em parceria com o Instituto Federal de Brasília [1]. 

Trata-se de um sistema web (com interface similar ao software *aSc TimeTables* [2, 3]) que visa automatizar, gerenciar e visualizar a grade horária acadêmica. O sistema permite a criação de grades através de matrizes visuais, alocação inteligente, prevenção de conflitos de horário e controle rigoroso de papéis e permissões institucionais [3-5].

## 🚀 Tecnologias Utilizadas

**Frontend:**
* React.js com Vite e TypeScript [6, 7]
* TailwindCSS (Estilização) [8]
* Axios e React Router DOM [9]
* React-DnD / dnd-kit (Funcionalidades de arrastar e soltar) [8]

**Backend:**
* Python + Django [8]
* Django REST Framework (API RESTful) [8]
* Banco de Dados: SQLite (Ambiente de Desenvolvimento) e PostgreSQL (Produção) [8]
* Autenticação via Tokens JWT (JSON Web Tokens) [4]

## 🏗️ Arquitetura do Sistema (Backend)
O backend adota uma arquitetura modular baseada em microsserviços internos, dividida nos seguintes aplicativos (`apps`) [10]:

* `core`: Configurações principais e roteamento geral.
* `people`: Gestão de Usuários com controle customizado de papéis (Coordenador Geral, Coordenador de Curso e Professor) e fluxos de autenticação [4].
* `courses`: Gerenciamento do CRUD das entidades fundamentais: Cursos, Turmas e Disciplinas [11, 12].
* `rooms`: Gerenciamento da infraestrutura física, Salas de aula, tipo e capacidades [13].
* `schedule`: Entidade central responsável pela alocação de "Aulas", eixos de tempo (dias da semana e horários) e fornecimento de dados para a matriz visual [14, 15].

## 🎯 Roadmap e Status de Desenvolvimento (Sprints)
O projeto está planejado para ser executado em 12 Sprints Semanais [3]:

* **✅ Sprints 1 e 2:** Fundação do sistema, configuração de ambiente (CORS, Vite, Django) e Autenticação protegida por papéis [4, 9, 16].
* **✅ Sprints 3 e 4:** Estruturação do banco de dados e APIs para o CRUD de Cursos, Turmas, Disciplinas, Professores e Salas [11, 13].
* **🔄 Sprint 5 e 6 (Fase Atual):** Modelagem da grade horária no backend e exibição da matriz semanal com componentes interativos no frontend [14, 15, 17].
* **⏳ Sprints 7 e 8:** Implementação de Drag-and-Drop e sistema de validação de conflitos em tempo real [5, 18].
* **⏳ Sprints 9 e 10:** Criação de fluxo de solicitações para professores e relatórios avançados (Dashboard e exportação para PDF) [19, 20].
* **⏳ Sprints 11 e 12:** Histórico de edições (Rollback), scripts de alocação inteligente e deploy em produção [21-23].

## ⚙️ Como Executar o Projeto Localmente

### Pré-requisitos
* Node.js e npm (Para o Frontend) [8]
* Python 3 e Virtualenv (Para o Backend) [8]

### 1. Inicializando o Backend (Django)
```bash
# Clone o repositório do backend
git clone https://github.com/Gerenciador-Academico-Org/GerenciadorAcademico.git

# Acesse a pasta do projeto e ative o ambiente virtual
cd GerenciadorAcademico
.\venv\Scripts\Activate.ps1   # No Windows [24]
source venv/bin/activate      # No Linux/Mac

# Instale as dependências (Django, DRF, Corsheaders, etc.)
pip install -r requirements.txt

# Execute as migrações para criar o banco de dados
python manage.py makemigrations
python manage.py migrate

# Inicie o servidor
python manage.py runserver
# O servidor rodará em http://127.0.0.1:8000/
2. Inicializando o Frontend (React/Vite)
# Clone o repositório do frontend
git clone https://github.com/Nicollascod/Residencia-Projeto.git

# Acesse a pasta do projeto
cd Residencia-Projeto

# Instale os pacotes NPM
npm install

# Inicie o servidor de desenvolvimento
npm run dev
# O sistema abrirá em http://localhost:5173/ [25]
👨‍💻 Equipe Desenvolvedora
Nicollas (Nicollascod) - Desenvolvimento Frontend (React)
Cleber Moreira (moreiradarocha) - Desenvolvimento Backend (Python/Django)
 e Arquitetura de Banco de Dados.

--------------------------------------------------------------------------------
Desenvolvido durante o programa Bolsa Futuro Digital - 2026
