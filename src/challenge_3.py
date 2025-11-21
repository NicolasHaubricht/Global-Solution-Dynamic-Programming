# -*- coding: utf-8 -*-
"""
Módulo para o Desafio 3: Pivô Mais Rápido.
Implementa uma solução gulosa baseada na razão Valor/Tempo (V/T) e uma
solução ótima por busca exaustiva para comparação.
"""
from itertools import combinations
from ..data import get_habilidades, get_base_skills

# Constantes do Desafio 3
ADAPTABILIDADE_MINIMA = 15

def greedy_selection(base_skills, habilidades):
    """
    Seleciona habilidades de nível básico usando uma abordagem gulosa,
    priorizando a maior razão Valor/Tempo (V/T).

    Returns:
        tuple: (caminho_selecionado, valor_total, tempo_total)
    """
    # List comprehension para calcular a razão V/T para cada habilidade base
    skills_with_ratio = [
        {
            **habilidades[skill_id],
            'ID': skill_id,
            'Ratio': habilidades[skill_id]['Valor'] / habilidades[skill_id]['Tempo']
        }
        for skill_id in base_skills
    ]

    # Ordena as habilidades pela razão V/T em ordem decrescente
    skills_with_ratio.sort(key=lambda x: x['Ratio'], reverse=True)

    selected_path = []
    total_value = 0
    total_time = 0

    for skill in skills_with_ratio:
        if total_value < ADAPTABILIDADE_MINIMA:
            selected_path.append(skill['ID'])
            total_value += skill['Valor']
            total_time += skill['Tempo']

    return selected_path, total_value, total_time

def exhaustive_search(base_skills, habilidades):
    """
    Encontra a solução ótima por busca exaustiva, testando todas as
    combinações de subconjuntos de habilidades básicas.

    Returns:
        tuple: (caminho_otimo, valor_otimo, tempo_otimo)
    """
    optimal_path = []
    optimal_time = float('inf')
    optimal_value = 0

    # Gera todas as combinações de subconjuntos de habilidades básicas
    for i in range(1, len(base_skills) + 1):
        # List comprehension para iterar sobre as combinações
        for subset in combinations(base_skills, i):
            # List comprehensions para calcular valor e tempo do subconjunto
            current_value = sum(habilidades[s]['Valor'] for s in subset)
            current_time = sum(habilidades[s]['Tempo'] for s in subset)

            if current_value >= ADAPTABILIDADE_MINIMA:
                # Critério de otimalidade: menor tempo
                if current_time < optimal_time:
                    optimal_time = current_time
                    optimal_value = current_value
                    optimal_path = list(subset)
                # Critério de desempate: se o tempo for igual, escolhe o de maior valor
                elif current_time == optimal_time and current_value > optimal_value:
                    optimal_value = current_value
                    optimal_path = list(subset)

    return optimal_path, optimal_value, optimal_time

def solve_challenge_3():
    """
    Resolve o Desafio 3: Pivô Mais Rápido.
    Compara a solução gulosa com a solução ótima por busca exaustiva.
    """
    habilidades = get_habilidades()
    base_skills = get_base_skills()

    # 1. Solução Gulosa
    greedy_path, greedy_value, greedy_time = greedy_selection(base_skills, habilidades)

    # 2. Solução Ótima (Busca Exaustiva)
    optimal_path, optimal_value, optimal_time = exhaustive_search(base_skills, habilidades)

    # 3. Comparação e Contraexemplo
    is_greedy_optimal = (greedy_time == optimal_time)

    # O contraexemplo é a própria comparação dos resultados, se forem diferentes.
    contraexemplo = None
    if not is_greedy_optimal:
        contraexemplo = {
            'Descrição': "A solução gulosa nem sempre é ótima. Neste caso, a busca exaustiva encontrou uma combinação de habilidades com menor tempo total para atingir a adaptabilidade mínima.",
            'Solução Gulosa': {'Caminho': greedy_path, 'Valor': greedy_value, 'Tempo': greedy_time},
            'Solução Ótima': {'Caminho': optimal_path, 'Valor': optimal_value, 'Tempo': optimal_time}
        }

    return {
        'Status': 'Sucesso',
        'Solução Gulosa': {'Caminho': greedy_path, 'Valor': greedy_value, 'Tempo': greedy_time},
        'Solução Ótima': {'Caminho': optimal_path, 'Valor': optimal_value, 'Tempo': optimal_time},
        'Gulosa é Ótima?': is_greedy_optimal,
        'Contraexemplo': contraexemplo,
        'Discussão de Complexidade': "A heurística gulosa (O(N log N) devido à ordenação) é muito mais rápida que a busca exaustiva (O(2^N)), sendo aceitável para um grande número de habilidades base, onde a solução ótima é computacionalmente inviável. No entanto, não garante a otimalidade."
    }

import matplotlib.pyplot as plt

def plot_greedy_vs_optimal(time_greedy, time_optimal):
    plt.figure(figsize=(10,6))
    
    bars = plt.bar(
        ["Gulosa", "Ótima"],
        [time_greedy, time_optimal],
        edgecolor="#1B4F72",
        linewidth=2,
        color=["#5DADE2", "#1B4F72"]
    )
    
    plt.title("Comparação dos Tempos – Gulosa vs Ótima", fontsize=16)
    plt.ylabel("Tempo Total (h)", fontsize=12)
    
    for bar in bars:
        plt.text(
            bar.get_x() + bar.get_width()/2,
            bar.get_height() + 0.1,
            f"{bar.get_height():.2f}h",
            ha="center",
            fontsize=12
        )
    
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()
