# -*- coding: utf-8 -*-
"""
Módulo para o Desafio 1: Caminho de Valor Máximo.
Utiliza Programação Dinâmica (DP) para a solução determinística e
Simulação de Monte Carlo para a solução com incerteza.
"""

import random
import numpy as np
from functools import lru_cache
from ..data import get_habilidades

# ==============================
# Constantes
# ==============================
TEMPO_MAX = 350
COMPLEXIDADE_MAX = 30
NUM_CENARIOS = 1000
TARGET_SKILL = "S6"


# ==============================
# 1. DP: Encontrar o conjunto de habilidades necessário
# ==============================
@lru_cache(maxsize=None)
def find_optimal_path_set(skill_id):
    """
    Calcula recursivamente o conjunto de habilidades exigido para atingir 'skill_id',
    retornando os acumulados: (valor_total, tempo_total, complexidade_total, conjunto_habilidades).
    """

    habilidades = get_habilidades()
    skill = habilidades.get(skill_id)

    # Habilidade inexistente
    if skill is None:
        return 0, 0, 0, frozenset()

    valor = skill["Valor"]
    tempo = skill["Tempo"]
    complexidade = skill["Complexidade"]
    prereqs = skill["Pre_Reqs"]

    # Caso base: habilidade sem pré-requisitos
    if not prereqs:
        return valor, tempo, complexidade, frozenset({skill_id})

    # Acumula valores da própria habilidade
    total_value = valor
    total_time = tempo
    total_complexity = complexidade
    path_set = {skill_id}

    # Obtém resultados dos pré-requisitos (memoizados)
    prereq_results = [find_optimal_path_set(p) for p in prereqs]

    for v, t, c, req_set in prereq_results:
        # Calcula apenas habilidades novas (evita contagem duplicada)
        new_skills = req_set - path_set

        # Soma incremental
        if new_skills:
            total_value += sum(habilidades[s]["Valor"] for s in new_skills)
            total_time += sum(habilidades[s]["Tempo"] for s in new_skills)
            total_complexity += sum(habilidades[s]["Complexidade"] for s in new_skills)

        # Atualiza caminho
        path_set.update(req_set)

    return total_value, total_time, total_complexity, frozenset(path_set)


# ==============================
# 2. Monte Carlo
# ==============================
def _simulate_scenario(habilidades, path_set):
    """
    Simula um cenário com variação de  ±10% no valor das habilidades.
    Retorna o valor total simulado do caminho.
    """

    # Gera uma perturbação para cada skill do caminho
    return sum(
        habilidades[s]["Valor"] * random.uniform(0.9, 1.1)
        for s in path_set
    )


# ==============================
# 3. Execução do desafio
# ==============================
def solve_challenge_1():
    """Executa a solução determinística e a versão com incerteza."""

    # Garante cache limpo
    find_optimal_path_set.cache_clear()

    habilidades = get_habilidades()

    # ----- Solução determinística -----
    total_value, total_time, total_complexity, path_frozen = find_optimal_path_set(TARGET_SKILL)
    path_set = set(path_frozen)

    if total_time > TEMPO_MAX or total_complexity > COMPLEXIDADE_MAX:
        det_result = {
            "Status": "Falha: Restrições excedidas",
            "Valor Total": 0,
            "Tempo Total": total_time,
            "Complexidade Total": total_complexity,
            "Caminho (Conjunto)": sorted(path_set)
        }
    else:
        det_result = {
            "Status": "Sucesso",
            "Valor Total": total_value,
            "Tempo Total": total_time,
            "Complexidade Total": total_complexity,
            "Caminho (Conjunto)": sorted(path_set)
        }

    # ----- Simulação de Monte Carlo -----
    simulated_values = [
        _simulate_scenario(habilidades, path_set)
        for _ in range(NUM_CENARIOS)
    ]

    mc_result = {
        "E[Valor total]": float(np.mean(simulated_values)),
        "Desvio Padrão": float(np.std(simulated_values)),
        "Número de Cenários": NUM_CENARIOS,
        "Valores Simulados": simulated_values
    }

    return det_result, mc_result



