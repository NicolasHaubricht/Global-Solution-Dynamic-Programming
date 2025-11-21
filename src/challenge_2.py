# -*- coding: utf-8 -*-
"""
Módulo para o Desafio 2: Verificação Crítica.
Utiliza permutações para enumerar todas as ordens de aquisição das habilidades críticas
e calcula o custo total (Tempo de Aquisição + Espera por pré-requisitos).
"""
from itertools import permutations
from ..data import get_habilidades, get_habilidades_criticas
from .graph_utils import validate_graph, GraphValidationError

def calculate_acquisition_cost(skill_order, habilidades):
    """
    Calcula o custo total (Tempo de Aquisição + Espera por pré-requisitos)
    para uma dada ordem de aquisição de habilidades.
    
    Args:
        skill_order (list): Lista de IDs de habilidades na ordem de aquisição.
        habilidades (dict): Dicionário mestre de habilidades.
        
    Returns:
        tuple: (custo_total, tempo_total_espera)
    """
    acquired_skills = set()
    total_cost = 0
    total_wait_time = 0
    
    for skill_id in skill_order:
        skill_data = habilidades.get(skill_id)
        if not skill_data:
            continue
            
        acquisition_time = skill_data['Tempo']
        prereqs = skill_data['Pre_Reqs']
        
        # List comprehension para verificar pré-requisitos não adquiridos
        missing_prereqs = [p for p in prereqs if p not in acquired_skills]
        
        # List comprehension para calcular o tempo de espera
        wait_time = sum(habilidades[p]['Tempo'] for p in missing_prereqs)
        
        total_wait_time += wait_time
        total_cost += acquisition_time + wait_time
        acquired_skills.add(skill_id)
        
    return total_cost, total_wait_time

def solve_challenge_2():
    """
    Resolve o Desafio 2: Verificação Crítica.
    """
    habilidades = get_habilidades()
    critical_skills = get_habilidades_criticas()
    
    # 1. Validação do Grafo (Exigência do Desafio)
    try:
        validate_graph()
    except GraphValidationError as e:
        return {
            'Status': 'Erro de Validação do Grafo',
            'Mensagem': str(e)
        }
        
    # 2. Enumeração das Permutações (120 permutações para 5 habilidades)
    all_permutations = list(permutations(critical_skills))
    
    # 3. Cálculo do Custo para Cada Permutação
    # List comprehension para calcular o custo de cada ordem
    results = [
        {
            'Ordem': list(order),
            'Custo Total': calculate_acquisition_cost(order, habilidades)[0],
            'Tempo de Espera': calculate_acquisition_cost(order, habilidades)[1]
        }
        for order in all_permutations
    ]
    
    # Ordena os resultados pelo Custo Total (menor é melhor)
    results.sort(key=lambda x: x['Custo Total'])
    
    # 4. Reporta as 3 melhores ordens
    top_3_results = results[:3]
    
    # Cálculo do custo médio das 3 melhores
    average_cost = sum(r['Custo Total'] for r in top_3_results) / 3
    
    return {
        'Status': 'Sucesso',
        'Total de Permutações': len(all_permutations),
        'Top 3 Melhores Ordens': top_3_results,
        'Custo Médio das Top 3': average_cost,
        'Heurística Observada': 'As melhores ordens tendem a priorizar habilidades com pré-requisitos já adquiridos ou com menor tempo de aquisição.'
    }

def plot_cost_comparison(top3):
    import matplotlib.pyplot as plt

    labels = [f"Ordem {i+1}" for i in range(len(top3))]
    custos = [item["Custo Total"] for item in top3]
    esperas = [item["Tempo de Espera"] for item in top3]

    plt.figure(figsize=(8, 5))
    plt.plot(labels, custos, marker='o', label="Custo Total (h)")
    plt.plot(labels, esperas, marker='o', label="Tempo de Espera (h)")

    plt.title("Comparação das Três Melhores Ordens")
    plt.xlabel("Ordens")
    plt.ylabel("Horas")
    plt.legend()
    plt.grid(True)

    plt.show()     # ← obrigatório no Jupyter
