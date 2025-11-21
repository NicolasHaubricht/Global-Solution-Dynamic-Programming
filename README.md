# 🌎 Global Solution | Dynamic Programming

Este repositório contém a implementação de um **Motor de Orientação de Habilidades (MOH)**, utilizando técnicas de Programação Dinâmica, Simulação de Monte Carlo e Busca Exaustiva para otimizar a aquisição de habilidades em um cenário de mercado dinâmico.

O projeto foi desenvolvido como parte de uma Global Solution e está estruturado de forma modularizada.

## 🧑‍💻 Integrantes

- Nicolas Haubricht Hainfellner - RM 556259
- Lucas henzo Ide Yuki - RM 554865

## ⚙️ Estrutura do Projeto

O código-fonte está distribuído nos seguintes módulos:

| Módulo | Responsabilidade |
| :--- | :--- |
| `dynamic_programming_project/data.py` | Definição da Estrutura de Dados Mestre (Habilidades). |
| `dynamic_programming_project/src/graph_utils.py` | Validação do Grafo de Pré-requisitos (Ciclos e Nós Órfãos). |
| `dynamic_programming_project/src/challenge_X.py` | Lógica de Negócio e Solução para cada Desafio (1 a 5). |
| `dynamic_programming_project/src/visual_utils.py` | Geração de Gráficos para visualização dos resultados. |
| `dynamic_programming.ipynb` | Notebook Jupyter com a execução e análise dos desafios. |

## 🚀 Como Executar o Código

O código pode ser executado diretamente no ambiente Python, seguindo os passos abaixo.

### 1. Pré-requisitos

Certifique-se de ter o Python 3.x instalado, juntamente com as bibliotecas necessárias.

```bash
# Instalar as bibliotecas necessárias
pip install pandas matplotlib
```

### 2. Estrutura de Arquivos

Para que o código de importação funcione corretamente, você deve replicar a estrutura de diretórios do projeto.

```
.
├── dynamic_programming_project/
│   ├── __init__.py
│   ├── data.py
│   └── src/
│       ├── __init__.py
│       ├── challenge_1.py
│       ├── challenge_2.py
│       ├── challenge_3.py
│       ├── challenge_4.py
│       ├── challenge_5.py
│       ├── graph_utils.py
│       └── visual_utils.py
└── run_challenges.py  # Arquivo de execução principal
```

### 3. Código Executável (`run_challenges.py`)

O código abaixo simula a execução do notebook, importando as funções e rodando os desafios em sequência. **Este é o código-fonte executável com as instruções de uso.**

Crie um arquivo chamado `run_challenges.py` e insira o seguinte conteúdo:

```python
import sys
import os
import json
import time
import matplotlib.pyplot as plt
import pandas as pd

# Adiciona o diretório pai ao path para importar os módulos
# Certifique-se de que a estrutura de diretórios está correta
sys.path.append(os.path.abspath('.'))

# Importa módulos de dados e utilidades
try:
    from dynamic_programming_project.data import get_habilidades
    from dynamic_programming_project.src.graph_utils import validate_graph, GraphValidationError
    from dynamic_programming_project.src.visual_utils import plot_monte_carlo_results, plot_cost_comparison, plot_greedy_vs_optimal
    
    # Importa módulos dos desafios
    from dynamic_programming_project.src.challenge_1 import solve_challenge_1
    from dynamic_programming_project.src.challenge_2 import solve_challenge_2
    from dynamic_programming_project.src.challenge_3 import solve_challenge_3
    from dynamic_programming_project.src.challenge_4 import solve_challenge_4
    from dynamic_programming_project.src.challenge_5 import solve_challenge_5
except ImportError as e:
    print(f"ERRO: Não foi possível importar um módulo. Verifique a estrutura de diretórios e se todos os arquivos .py estão presentes.")
    print(f"Detalhes do erro: {e}")
    sys.exit(1)


def run_validation():
    """Executa a validação inicial do grafo de pré-requisitos."""
    print("\n--- Validação Inicial do Grafo de Pré-requisitos ---")
    try:
        orphan_res, cycle_res = validate_graph()
        print(f"Nós Órfãos: {orphan_res}")
        print(f"Ciclos: {cycle_res}")
        print("Grafo validado com sucesso. Podemos prosseguir com os desafios.")
        return True
    except GraphValidationError as e:
        print(f"ERRO DE VALIDAÇÃO CRÍTICO: {e}")
        print("A execução dos desafios será interrompida.")
        return False

def run_challenge_1():
    """Desafio 1: Caminho de Valor Máximo (DP e Monte Carlo)"""
    print("\n\n--- 🖥️ Desafio 1: Caminho de Valor Máximo ---")
    results_1 = solve_challenge_1()
    
    print("\n=== RESULTADO DETERMINÍSTICO ===")
    print(f"Status: {results_1['Status']}")
    print(f"Valor Total: {results_1['Valor Total']}")
    print(f"Tempo Total: {results_1['Tempo Total']}")
    print(f"Complexidade Total: {results_1['Complexidade Total']}")
    print(f"Caminho (Conjunto): {results_1['Caminho (Conjunto)']}")
    
    print("\n=== RESULTADO MONTE CARLO ===")
    print(f"Valor Esperado: {results_1['Valor Esperado']:.2f}")
    print(f"Desvio Padrão: {results_1['Desvio Padrão']:.2f}")
    print(f"Nº de Cenários: {results_1['Nº de Cenários']}")
    
    # Gera o gráfico (se a função estiver implementada e o backend for compatível)
    try:
        plot_monte_carlo_results(results_1['Resultados Monte Carlo'])
    except Exception as e:
        print(f"Aviso: Não foi possível gerar o gráfico do Desafio 1. Erro: {e}")

def run_challenge_2():
    """Desafio 2: Sequência de Menor Custo (Busca Exaustiva)"""
    print("\n\n--- 🖥️ Desafio 2: Sequência de Menor Custo ---")
    results_2 = solve_challenge_2()
    
    print(f"Total de Permutações: {results_2['Total de Permutações']}")
    print(f"Custo Médio das Top 3: {results_2['Custo Médio das Top 3']:.2f}h")
    print(f"Heurística Observada: {results_2['Heurística Observada']}\n")
    
    print("=== TOP 3 MELHORES ORDENS ===")
    top3 = results_2["Top 3 Melhores Ordens"]
    for idx, item in enumerate(top3, start=1):
        print(
            f"{idx}. Ordem: {item['Ordem']} | "
            f"Custo Total: {item['Custo Total']}h | "
            f"Espera: {item['Tempo de Espera']}h")
    
    # Gera o gráfico
    try:
        plot_cost_comparison(top3)
    except Exception as e:
        print(f"Aviso: Não foi possível gerar o gráfico do Desafio 2. Erro: {e}")

def run_challenge_3():
    """Desafio 3: Pivô Mais Rápido (Guloso vs. Ótimo)"""
    print("\n\n--- 🖥️ Desafio 3: Pivô Mais Rápido ---")
    results_3 = solve_challenge_3()
    
    print(f"Status: {results_3['Status']}")
    print("\n--- Solução Gulosa ---")
    print(f"Caminho: {results_3['Solução Gulosa']['Caminho']}")
    print(f"Valor: {results_3['Solução Gulosa']['Valor']}")
    print(f"Tempo: {results_3['Solução Gulosa']['Tempo']}h")
    
    print("\n--- Solução Ótima ---")
    print(f"Caminho: {results_3['Solução Ótima']['Caminho']}")
    print(f"Valor: {results_3['Solução Ótima']['Valor']}")
    print(f"Tempo: {results_3['Solução Ótima']['Tempo']}h")
    
    print(f"\nGulosa é Ótima? {results_3['Gulosa é Ótima?']}")
    print(f"Discussão: {results_3['Discussão de Complexidade']}")
    
    # Gera o gráfico
    try:
        plot_greedy_vs_optimal(results_3['Solução Gulosa']['Tempo'], results_3['Solução Ótima']['Tempo'])
    except Exception as e:
        print(f"Aviso: Não foi possível gerar o gráfico do Desafio 3. Erro: {e}")

def run_challenge_4():
    """Desafio 4: Otimização de Recursos (Busca Exaustiva)"""
    print("\n\n--- 🖥️ Desafio 4: Otimização de Recursos ---")
    results_4 = solve_challenge_4()
    
    print(f"Status: {results_4['Status']}")
    print(f"Valor Máximo: {results_4['Valor Máximo']}")
    print(f"Tempo Total: {results_4['Tempo Total']}h")
    print(f"Complexidade Total: {results_4['Complexidade Total']}")
    print(f"Caminho Ótimo: {results_4['Caminho Ótimo']}")
    print(f"Total de Combinações Verificadas: {results_4['Total de Combinações Verificadas']}")
    print(f"Tempo de Execução: {results_4['Tempo de Execução']:.4f}s")

def run_challenge_5():
    """Desafio 5: Recomendação de Próximas Habilidades (DP com Pré-requisitos)"""
    print("\n\n--- 🖥️ Desafio 5: Recomendação de Próximas Habilidades ---")
    # Exemplo de execução com habilidades iniciais 'S1' e 'S2'
    current_skills_list = ['S1', 'S2']
    resultado = solve_challenge_5(current_skills_list=current_skills_list)
    
    print("=== Desafio 5 – Recomendar Próximas Habilidades ===")
    print(f"Status: {resultado['Status']}")
    print(f"Perfil Atual: {resultado['Perfil Atual']}")
    print(f"Horizonte de Recomendação: {resultado['Horizonte de Recomendação']}")
    print(f"Valor Esperado Máximo (Estimado): {resultado['Valor Esperado Máximo (Estimado)']:.2f}")
    print()
    
    # Exibir habilidades recomendadas em tabela
    if resultado['Habilidades Recomendadas']:
        df_recomendadas = pd.DataFrame({
            'Ordem': range(1, len(resultado['Habilidades Recomendadas']) + 1),
            'Habilidade Recomendada': resultado['Habilidades Recomendadas']
        })
        print(df_recomendadas.to_markdown(index=False))
    else:
        print("Nenhuma habilidade recomendada encontrada.")


if __name__ == "__main__":
    if run_validation():
        run_challenge_1()
        run_challenge_2()
        run_challenge_3()
        run_challenge_4()
        run_challenge_5()
        
        # Manter os gráficos abertos (opcional, dependendo do ambiente)
        # plt.show() 
        print("\n\n--- Execução Concluída ---")

```

### 4. Execução

1.  Salve o código acima como `run_challenges.py` no diretório raiz do projeto.
2.  Preencha os arquivos `.py` dentro da estrutura `dynamic_programming_project/` com o código-fonte correspondente (que deve ser extraído do notebook original ou fornecido separadamente).
3.  Execute o script:

```bash
python run_challenges.py
```

O script irá imprimir os resultados de cada desafio no console e, se o ambiente for gráfico, tentará exibir os gráficos gerados.
