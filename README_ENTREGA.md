# Gerenciador Acadêmico

Sistema Inteligente de Gerenciamento de Salas e Horários Acadêmicos.

## Recursos principais

- Cadastro de cursos, turmas, disciplinas, professores e salas
- Grade horária visual
- Validação de conflitos de professor, turma e sala
- Validação de capacidade da sala
- Solicitações de ajustes
- Dashboard geral
- API REST
- Área administrativa Django

## Executar o projeto

```powershell
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Acessos

Página inicial:

```text
http://127.0.0.1:8000/
```

Administração:

```text
http://127.0.0.1:8000/admin/
```

Grade visual:

```text
http://127.0.0.1:8000/grade/
```

API:

```text
http://127.0.0.1:8000/api/
```

## Estrutura

```text
core/
setup/
manage.py
requirements.txt
```
