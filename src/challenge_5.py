# Conteúdo CORRIGIDO para dynamic_programming_project/src/challenge_5.py

# -*- coding: utf-8 -*-
"""
Módulo para o Desafio 5: Recomendar Próximas Habilidades.
Utiliza Programação Dinâmica (DP) com "look ahead" para sugerir as próximas
habilidades que maximizam o valor esperado em um horizonte de 5 anos.
"""
from functools import lru_cache
from ..data import get_habilidades

# Constantes do Desafio 5
HORIZONTE_ANOS = 5
MAX_SKILLS_TO_RECOMMEND = 3

def get_available_skills(acquired_skills, habilidades):
    """
    Retorna as habilidades que podem ser adquiridas (pré-requisitos satisfeitos).
    """
    # List comprehension para filtrar habilidades disponíveis
    available = [
        skill_id for skill_id, data in habilidades.items()
        if skill_id not in acquired_skills and all(prereq in acquired_skills for prereq in data['Pre_Reqs'])
    ]
    return available

@lru_cache(maxsize=None)
def dp_recommendation(current_skills_tuple, remaining_steps, market_transition_prob_tuple):
    """
    Função recursiva com memoização (DP) para encontrar o valor máximo esperado
    em um horizonte de tempo (remaining_steps).
    
    Args:
        current_skills_tuple (tuple): Tupla de IDs das habilidades adquiridas (estado hashable).
        remaining_steps (int): Número de habilidades restantes para recomendar.
        market_transition_prob_tuple (tuple): Tupla hashable das probabilidades de mercado.
        
    Returns:
        tuple: (valor_maximo_esperado, melhor_proxima_habilidade)
    """
    if remaining_steps == 0:
        return 0, None

    habilidades = get_habilidades() # Acessa o dicionário de habilidades aqui
    current_skills = set(current_skills_tuple)
    available_skills = get_available_skills(current_skills, habilidades)
    
    # Converte a tupla de probabilidades de volta para um dicionário para fácil acesso
    market_transition_prob = dict(market_transition_prob_tuple)
    
    max_expected_value = -1
    best_next_skill = None

    # Se não houver habilidades disponíveis, retorna 0
    if not available_skills:
        return 0, None

    for next_skill in available_skills:
        skill_data = habilidades[next_skill]
        
        # Valor da habilidade atual
        base_value = skill_data['Valor']
        
        # Fator de ponderação (probabilidade de transição de mercado)
        prob_factor = market_transition_prob.get(next_skill, 1.0)
        
        # Novo estado após adquirir a habilidade (deve ser hashable)
        new_skills_tuple = tuple(sorted(list(current_skills) + [next_skill]))
        
        # Chamada recursiva (look ahead) ajustada
        future_expected_value, _ = dp_recommendation(
            new_skills_tuple,
            remaining_steps - 1,
            market_transition_prob_tuple
        )
        
        # Valor esperado total: (Valor Base * Fator Prob.) + Valor Esperado Futuro
        expected_value = (base_value * prob_factor) + future_expected_value
        
        if expected_value > max_expected_value:
            max_expected_value = expected_value
            best_next_skill = next_skill

    return max_expected_value, best_next_skill

def solve_challenge_5(current_skills_list=None):
    """
    Resolve o Desafio 5: Recomendar Próximas Habilidades.
    """
    # Limpa o cache da DP antes de resolver
    dp_recommendation.cache_clear()
    
    # Define o perfil atual (exemplo: S1 e S2 adquiridas)
    if current_skills_list is None:
        current_skills_list = ['S1', 'S2']
        
    current_skills_tuple = tuple(sorted(current_skills_list))
    
    # Simulação de Probabilidades de Transição de Mercado (fictício para demonstração)
    market_transition_prob = {
        'S6': 1.5, # IA Generativa (Objetivo Final)
        'S9': 1.3, # DevOps & CI/CD (Crítica)
        'S7': 1.2, # Estruturas em Nuvem (Crítica)
        'S4': 1.1, # ML (Não Crítica, mas alta Complexidade)
    }
    
    # Converte o dicionário de probabilidades para uma tupla de tuplas (hashable)
    market_transition_prob_tuple = tuple(sorted(market_transition_prob.items()))
    
    recommendations = []
    current_state = current_skills_tuple
    max_expected_value = 0
    
    # Loop para encontrar as 3 melhores habilidades em sequência
    for step in range(MAX_SKILLS_TO_RECOMMEND):
        # Chamada ajustada
        max_expected_value, best_next_skill = dp_recommendation(
            current_state,
            MAX_SKILLS_TO_RECOMMEND - step, # Passos restantes
            market_transition_prob_tuple
        )
        
        if best_next_skill:
            recommendations.append(best_next_skill)
            # Atualiza o estado para a próxima iteração
            current_state = tuple(sorted(list(current_state) + [best_next_skill]))
        else:
            break
            
    return {
        'Status': 'Sucesso',
        'Perfil Atual': current_skills_list,
        'Horizonte de Recomendação': f'{HORIZONTE_ANOS} anos ({MAX_SKILLS_TO_RECOMMEND} habilidades)',
        'Habilidades Recomendadas': recommendations,
        'Valor Esperado Máximo (Estimado)': max_expected_value
    }
