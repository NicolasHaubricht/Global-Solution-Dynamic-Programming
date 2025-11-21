# -*- coding: utf-8 -*-
"""
Módulo de utilidades para geração de gráficos e visualizações.
"""
import matplotlib.pyplot as plt
import numpy as np
import io
import base64

# Configuração para evitar problemas de backend em ambientes sem display
plt.switch_backend('Agg')

def plot_monte_carlo_results(simulated_values, expected_value, std_dev):
    """
    Gera um histograma dos resultados da simulação de Monte Carlo.
    Retorna o HTML para exibição no notebook.
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Histograma dos valores simulados
    ax.hist(simulated_values, bins=50, density=True, alpha=0.6, color='skyblue', label='Distribuição de Valor')
    
    # Linha do Valor Esperado (Média)
    ax.axvline(expected_value, color='red', linestyle='dashed', linewidth=2, label=f'E[Valor] = {expected_value:.2f}')
    
    # Linhas de Desvio Padrão
    ax.axvline(expected_value + std_dev, color='orange', linestyle='dotted', linewidth=1, label=f'± 1 Desvio Padrão')
    ax.axvline(expected_value - std_dev, color='orange', linestyle='dotted', linewidth=1)
    
    ax.set_title('Distribuição de Valor Total do Caminho (Simulação de Monte Carlo)', fontsize=14)
    ax.set_xlabel('Valor Total', fontsize=12)
    ax.set_ylabel('Densidade', fontsize=12)
    ax.legend()
    ax.grid(axis='y', alpha=0.5)
    
    # Salva o gráfico em um buffer e codifica para base64
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    plt.close(fig)
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    
    # Retorna o HTML para exibição no notebook
    return f'<img src="data:image/png;base64,{data}"/>'

def plot_cost_comparison(results):
    """
    Gera um gráfico de barras comparando o custo total das 3 melhores ordens.
    Retorna o HTML para exibição no notebook.
    """
    orders = [f"Ordem {i+1}" for i in range(len(results))]
    costs = [r['Custo Total'] for r in results]
    wait_times = [r['Tempo de Espera'] for r in results]
    acquisition_times = [c - w for c, w in zip(costs, wait_times)]
    
    x = np.arange(len(orders))
    width = 0.35
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Barras de Tempo de Aquisição
    rects1 = ax.bar(x - width/2, acquisition_times, width, label='Tempo de Aquisição', color='skyblue')
    # Barras de Tempo de Espera (empilhadas)
    rects2 = ax.bar(x + width/2, wait_times, width, label='Tempo de Espera (Custo Adicional)', color='salmon')
    
    ax.set_ylabel('Tempo (Horas)', fontsize=12)
    ax.set_title('Comparação de Custo Total (Aquisição + Espera) das Top 3 Ordens', fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(orders)
    ax.legend()
    
    # Adiciona o custo total acima das barras
    for i, cost in enumerate(costs):
        ax.text(x[i], cost + 5, f'{cost}', ha='center', va='bottom', fontsize=10)
        
    # Salva o gráfico em um buffer e codifica para base64
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    plt.close(fig)
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    
    return f'<img src="data:image/png;base64,{data}"/>'

def plot_greedy_vs_optimal(greedy_time, optimal_time):
    """
    Gera um gráfico de barras comparando o tempo da solução gulosa vs. ótima.
    Retorna o HTML para exibição no notebook.
    """
    labels = ['Solução Gulosa', 'Solução Ótima']
    times = [greedy_time, optimal_time]
    colors = ['lightcoral', 'mediumseagreen']
    
    fig, ax = plt.subplots(figsize=(8, 5))
    
    ax.bar(labels, times, color=colors)
    ax.set_ylabel('Tempo Total (Horas)', fontsize=12)
    ax.set_title('Comparação de Tempo: Guloso vs. Ótimo (Valor ≥ 15)', fontsize=14)
    
    # Adiciona o valor do tempo nas barras
    for i, time in enumerate(times):
        ax.text(i, time + 1, f'{time}', ha='center', va='bottom', fontsize=10)
        
    # Salva o gráfico em um buffer e codifica para base64
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    plt.close(fig)
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    
    return f'<img src="data:image/png;base64,{data}"/>'
