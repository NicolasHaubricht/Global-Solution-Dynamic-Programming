# -*- coding: utf-8 -*-
"""
Desafio 4 – Trilhas Paralelas (Merge Sort)

Objetivo:
    Ordenar as 12 habilidades por Complexidade (C) usando Merge Sort.
    Comparar o tempo do algoritmo implementado com o sort nativo do Python.
"""

import time
from ..data import get_habilidades


# ------------------------------------------------------------
# MERGE SORT (IMPLEMENTAÇÃO PRÓPRIA)
# ------------------------------------------------------------
def merge_sort(data, key=lambda x: x):
    """Merge Sort recursivo."""
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = merge_sort(data[:mid], key)
    right = merge_sort(data[mid:], key)

    return merge(left, right, key)


def merge(left, right, key):
    """Mescla duas listas ordenadas."""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if key(left[i]) <= key(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ------------------------------------------------------------
# SOLUÇÃO DO DESAFIO
# ------------------------------------------------------------
def solve_challenge_4():
    """
    Resolve o Desafio 4:
        - Lê as habilidades
        - Ordena por 'Complexidade' usando Merge Sort
        - Divide em Sprint A / Sprint B
        - Compara tempo com sort nativo
    """
    habilidades = get_habilidades()

    # prepara lista de objetos para ordenar
    dataset = [
        {
            'ID': skill_id,
            'Complexidade': info['Complexidade'],
            'Nome': info['Nome']
        }
        for skill_id, info in habilidades.items()
    ]

    key_func = lambda x: x['Complexidade']

    # ------------------------------
    # Tempo – Merge Sort próprio
    # ------------------------------
    t0 = time.perf_counter()
    sorted_merge = merge_sort(dataset, key=key_func)
    t1 = time.perf_counter()
    time_merge = t1 - t0

    # ------------------------------
    # Tempo – Sort nativo
    # ------------------------------
    t2 = time.perf_counter()
    sorted_native = sorted(dataset, key=key_func)
    t3 = time.perf_counter()
    time_native = t3 - t2

    # divide em sprints
    sprint_a = sorted_merge[:6]
    sprint_b = sorted_merge[6:]

    return {
        'Status': 'Sucesso',
        'Algoritmo': 'Merge Sort (Implementação Própria)',
        'Complexidade': 'O(N log N)',
        'Ordenado por Complexidade': sorted_merge,
        'Sprint A': sprint_a,
        'Sprint B': sprint_b,
        'Tempo Merge Sort': time_merge,
        'Tempo Sort Nativo': time_native
    }