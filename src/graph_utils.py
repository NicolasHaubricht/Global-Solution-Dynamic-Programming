# -*- coding: utf-8 -*-
"""
Módulo de utilidades para manipulação e validação do grafo de habilidades.
Inclui funções para detecção de ciclos e nós órfãos.
"""
from ..data import get_habilidades

class GraphValidationError(Exception):
    """Exceção personalizada para erros de validação do grafo."""
    pass

def build_prerequisite_graph(habilidades):
    """
    Constrói o grafo de pré-requisitos a partir do dicionário de habilidades.
    O grafo é um dicionário onde a chave é a habilidade e o valor é uma lista
    de seus pré-requisitos (arestas de entrada).
    """
    # List comprehension para construir o grafo
    graph = {skill_id: data['Pre_Reqs'] for skill_id, data in habilidades.items()}
    return graph

def _dfs_cycle_check(node, graph, visited, recursion_stack, path):
    """
    Função auxiliar recursiva para detecção de ciclos usando DFS.
    
    visited: set de nós visitados (totalmente processados).
    recursion_stack: set de nós na pilha de recursão atual (em processamento).
    path: lista de nós no caminho atual para reportar o ciclo.
    """
    visited.add(node)
    recursion_stack.add(node)
    path.append(node)

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            # Chamada recursiva
            if _dfs_cycle_check(neighbor, graph, visited, recursion_stack, path):
                return True
        elif neighbor in recursion_stack:
            # Ciclo detectado. neighbor é o nó que já está na pilha de recursão.
            cycle_start_index = path.index(neighbor)
            cycle = path[cycle_start_index:]
            raise GraphValidationError(f"Ciclo detectado: {' -> '.join(cycle)} -> {neighbor}")

    recursion_stack.remove(node)
    path.pop()
    return False

def check_for_cycles(graph):
    """
    Verifica a existência de ciclos no grafo de pré-requisitos.
    Utiliza DFS e recursão.
    """
    visited = set()
    recursion_stack = set()
    
    for node in graph:
        if node not in visited:
            try:
                _dfs_cycle_check(node, graph, visited, recursion_stack, [])
            except GraphValidationError as e:
                # Re-lança a exceção para ser tratada externamente
                raise e
    
    return "Nenhum ciclo detectado."

def check_for_orphan_nodes(graph, all_skills):
    """
    Verifica se há pré-requisitos que não existem na lista de habilidades (nós órfãos).
    """
    orphan_nodes = set()
    for skill, prereqs in graph.items():
        # List comprehension para encontrar pré-requisitos órfãos
        orphans = [prereq for prereq in prereqs if prereq not in all_skills]
        orphan_nodes.update(orphans)
        
    if orphan_nodes:
        raise GraphValidationError(f"Nós órfãos detectados (pré-requisitos inexistentes): {', '.join(orphan_nodes)}")
    
    return "Nenhum nó órfão detectado."

def validate_graph():
    """
    Função principal para validar o grafo de habilidades.
    """
    habilidades = get_habilidades()
    graph = build_prerequisite_graph(habilidades)
    all_skills = set(habilidades.keys())
    
    # 1. Checar nós órfãos
    orphan_result = check_for_orphan_nodes(graph, all_skills)
    
    # 2. Checar ciclos
    cycle_result = check_for_cycles(graph)
    
    return orphan_result, cycle_result
