import json
from ortools.sat.python import cp_model

def carregar_dados(caminho):
    with open(caminho, 'r', encoding='utf-8') as f:
        return json.load(f)

def resolver_horario_profissional():
    dados = carregar_dados('dados.json')
    modelo = cp_model.CpModel()
    
    profs = dados['professores']
    salas = dados['salas']
    horas = dados['horarios']
    discs = dados['disciplinas']
    restricoes = dados.get('restricoes', {})

    # 1. CRIAR AS VARIÁVEIS (O MAPA DE POSSIBILIDADES)
    alocacoes = {}
    for p in profs:
        for d in discs:
            for s in salas:
                for h in horas:
                    alocacoes[(p, d, s, h)] = modelo.NewBoolVar(f'{p}_{d}_{s}_{h}')

    # 2. REGRAS RÍGIDAS (AS BÁSICAS)
    for d in discs:
        modelo.Add(sum(alocacoes[(p, d, s, h)] for p in profs for s in salas for h in horas) == 1)

    for p in profs:
        for h in horas:
            modelo.Add(sum(alocacoes[(p, d, s, h)] for d in discs for s in salas) <= 1)

    for s in salas:
        for h in horas:
            modelo.Add(sum(alocacoes[(p, d, s, h)] for p in profs for d in discs) <= 1)

    # 3. REGRAS DE NEGÓCIO (AS COMPLEXAS)
    
    # Indisponibilidade: "Professor X não pode no Horário Y"
    indisp = restricoes.get('indisponibilidade', {})
    for prof_nome, horarios_proibidos in indisp.items():
        for h_proibido in horarios_proibidos:
            # Forçamos a soma de todas as aulas desse prof nesse horário a ser ZERO
            modelo.Add(sum(alocacoes[(prof_nome, d, s, h_proibido)] for d in discs for s in salas) == 0)

    # Obrigatoriedade de Sala: "Disciplina X tem que ser na Sala Y"
    obrigatoria = restricoes.get('obrigatoriedade_sala', {})
    for disc_nome, sala_obrigatoria in obrigatoria.items():
        for p in profs:
            for s in salas:
                for h in horas:
                    if s != sala_obrigatoria:
                        # Se a sala não for a correta, essa possibilidade é ZERO
                        modelo.Add(alocacoes[(p, disc_nome, s, h)] == 0)

    # 4. SOLVER
    resolutor = cp_model.CpSolver()
    status = resolutor.Solve(modelo)

    # 5. IMPRESSÃO
    if status in [cp_model.OPTIMAL, cp_model.FEASIBLE]:
        print(f"{'HORA':<8} | {'SALA':<15} | {'PROFESSOR':<15} | {'DISCIPLINA'}")
        print("-" * 60)
        for h in horas:
            for s in salas:
                for p in profs:
                    for d in discs:
                        if resolutor.Value(alocacoes[(p, d, s, h)]) == 1:
                            print(f"{h:<8} | {s:<15} | {p:<15} | {d}")
    else:
        print("Impossível organizar com as restrições atuais!")

resolver_horario_profissional()