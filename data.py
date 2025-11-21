# -*- coding: utf-8 -*-
"""
Módulo de dados mestre para o projeto de Dynamic Programming.
Contém a definição das habilidades e seus metadados.
"""

HABILIDADES_MESTRE = {
    'S1': {'Nome': 'Programação Básica (Python)', 'Tempo': 80, 'Valor': 3, 'Complexidade': 4, 'Pre_Reqs': [], 'Uso': 'Base'},
    'S2': {'Nome': 'Modelagem de Dados (SQL)', 'Tempo': 60, 'Valor': 4, 'Complexidade': 3, 'Pre_Reqs': [], 'Uso': 'Base'},
    'S3': {'Nome': 'Algoritmos Avançados (HC1)', 'Tempo': 100, 'Valor': 7, 'Complexidade': 8, 'Pre_Reqs': ['S1'], 'Uso': 'Crítica'},
    'S4': {'Nome': 'Fundamentos de Machine Learning', 'Tempo': 120, 'Valor': 8, 'Complexidade': 9, 'Pre_Reqs': ['S1', 'S3'], 'Uso': 'Não Crítica'},
    'S5': {'Nome': 'Visualização de Dados (BI) (HC2)', 'Tempo': 40, 'Valor': 6, 'Complexidade': 5, 'Pre_Reqs': ['S2'], 'Uso': 'Crítica'},
    'S6': {'Nome': 'IA Generativa Ética', 'Tempo': 150, 'Valor': 10, 'Complexidade': 10, 'Pre_Reqs': ['S4'], 'Uso': 'Objetivo Final'},
    'S7': {'Nome': 'Estruturas em Nuvem (AWS/Azure) (HC3)', 'Tempo': 70, 'Valor': 5, 'Complexidade': 7, 'Pre_Reqs': [], 'Uso': 'Crítica'},
    'S8': {'Nome': 'APIs e Microsserviços (HC4)', 'Tempo': 90, 'Valor': 6, 'Complexidade': 6, 'Pre_Reqs': ['S1'], 'Uso': 'Crítica'},
    'S9': {'Nome': 'DevOps & CI/CD (HC5)', 'Tempo': 110, 'Valor': 9, 'Complexidade': 8, 'Pre_Reqs': ['S7', 'S8'], 'Uso': 'Crítica'},
    'H10': {'Nome': 'Segurança de Dados', 'Tempo': 60, 'Valor': 5, 'Complexidade': 6, 'Pre_Reqs': [], 'Uso': 'Lista Grande'},
    'H11': {'Nome': 'Análise de Big Data', 'Tempo': 90, 'Valor': 8, 'Complexidade': 8, 'Pre_Reqs': ['S4'], 'Uso': 'Lista Grande'},
    'H12': {'Nome': 'Introdução a IoT', 'Tempo': 30, 'Valor': 3, 'Complexidade': 3, 'Pre_Reqs': [], 'Uso': 'Lista Grande'},
}

HABILIDADES_CRITICAS = ['S3', 'S5', 'S7', 'S8', 'S9']

def get_habilidades():
    """Retorna o dicionário mestre de habilidades."""
    return HABILIDADES_MESTRE

def get_habilidades_criticas():
    """Retorna a lista de IDs das habilidades críticas."""
    return HABILIDADES_CRITICAS

def get_base_skills():
    """Retorna as habilidades de nível básico (sem pré-requisitos)."""
    # List comprehension para filtrar habilidades sem pré-requisitos
    return [
        skill_id for skill_id, data in HABILIDADES_MESTRE.items()
        if not data['Pre_Reqs']
    ]

def get_skill_data(skill_id):
    """Retorna os dados de uma habilidade específica."""
    return HABILIDADES_MESTRE.get(skill_id)
