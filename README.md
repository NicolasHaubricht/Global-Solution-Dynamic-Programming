# Projeto de Otimização de Trilhas de Habilidades (GS_Nov25_DProg_AM)

Este projeto implementa soluções para os desafios de otimização de trilhas de habilidades, conforme especificado no documento `GS_Nov25_DProg_AM.pdf`. O código foi desenvolvido em Python, seguindo princípios de **modularização**, **boas práticas**, e utilizando técnicas avançadas como **memoização**, **recursão** e **list comprehension**.

## Estrutura do Projeto

O projeto está organizado de forma modular para garantir a clareza e a manutenibilidade:

```
dynamic_programming_project/
├── data.py                 # Módulo com a estrutura de dados mestre (HABILIDADES_MESTRE).
├── main_demonstration.ipynb # Notebook Jupyter para demonstração e execução dos desafios.
├── README.md               # Este arquivo.
└── src/
    ├── __init__.py         # Inicializador do módulo Python (vazio, mas necessário).
    ├── visual_utils.py     # Funções para geração de gráficos (Matplotlib).
    ├── graph_utils.py      # Validação do grafo (ciclos, nós órfãos) com recursão.
    ├── challenge_1.py      # Desafio 1: Caminho de Valor Máximo (DP e Monte Carlo).
    ├── challenge_2.py      # Desafio 2: Verificação Crítica (Permutações e Custo).
    ├── challenge_3.py      # Desafio 3: Pivô Mais Rápido (Guloso vs. Busca Exaustiva).
    ├── challenge_4.py      # Desafio 4: Trilhas Paralelas (Merge Sort implementado).
    └── challenge_5.py      # Desafio 5: Recomendar Habilidades (DP com Look Ahead).
```

## Como Executar

1.  **Pré-requisitos:** Certifique-se de ter o Python 3.x, o Jupyter Notebook/Lab e as bibliotecas `numpy` e `matplotlib` instaladas.
    ```bash
    pip install jupyter numpy matplotlib
    ```
2.  **Execução:** Abra o arquivo `main_demonstration.ipynb` em seu ambiente Jupyter.
3.  **Demonstração:** Execute as células do notebook sequencialmente. O notebook importa e executa as funções de cada módulo, apresentando os resultados e gráficos para cada desafio.

## Boas Práticas e Técnicas Utilizadas

| Técnica | Módulos de Aplicação | Descrição |
| :--- | :--- | :--- |
| **Modularização** | Todos os módulos em `src/` | Separação de responsabilidades por desafio e utilidade. |
| **Memoização (`@lru_cache`)** | `challenge_1.py`, `challenge_5.py` | Otimização de funções recursivas de Programação Dinâmica (DP). |
| **Recursão** | `graph_utils.py` (DFS), `challenge_4.py` (Merge Sort), `challenge_5.py` (DP) | Essencial para algoritmos de busca e divisão e conquista. |
| **List Comprehension** | Todos os módulos | Utilizada para criação concisa de listas, filtragem e mapeamento de dados. |
| **Estruturas de Dados** | `data.py`, `graph_utils.py` | Uso de Dicionários, Conjuntos e Tuplas imutáveis (`frozenset`) para estados de memoização. |
