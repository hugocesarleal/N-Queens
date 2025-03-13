# Algoritmo das N-Rainhas com Busca Tabu

Este repositório contém uma implementação do problema das N-Rainhas utilizando o algoritmo de Busca Tabu. O código foi desenvolvido como parte de um trabalho para a disciplina de Inteligência Artificial.

# Publicado em:
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14989076.svg)](https://doi.org/10.5281/zenodo.14989076)

## Descrição

O problema das N-Rainhas consiste em posicionar N rainhas em um tabuleiro de xadrez \(N \times N\) de forma que nenhuma rainha ataque outra. Isso significa que:
- Nenhuma rainha pode estar na mesma linha.
- Nenhuma rainha pode estar na mesma coluna.
- Nenhuma rainha pode estar na mesma diagonal.

Este projeto utiliza a técnica de **Busca Tabu**, um método heurístico para resolver problemas de otimização combinatória. A busca tabu evita ciclos ao manter uma lista de soluções recentemente visitadas ou movimentos proibidos por um determinado número de iterações.

## Funcionalidades

- Geração de uma solução inicial aleatória.
- Avaliação do número de conflitos usando a função objetivo.
- Geração de vizinhos ao trocar posições de rainhas.
- Busca iterativa até encontrar uma solução sem conflitos ou atingir o limite de iterações.
- Visualização do tabuleiro final utilizando a função `desenharTabuleiro`.

## Estrutura do Código

### Funções Principais

- `gerarSolucaoInicial(n)`: Gera uma solução inicial aleatória para o tabuleiro.
- `funcaoObjetivo(solucao)`: Avalia a solução, retornando o número de conflitos e as rainhas envolvidas.
- `gerarVizinho(solucao, rainhasConflito)`: Gera uma nova solução trocando posições de rainhas em conflito.
- `buscaTabu(n, iteracoesMax, rodarAteEncontrarZero)`: Implementa o algoritmo de Busca Tabu para resolver o problema.

### Execução Principal

No bloco principal (`if __name__ == "__main__"`), o programa:
1. Configura os parâmetros do problema.
2. Inicia o cronômetro para medir o tempo de execução.
3. Executa a Busca Tabu.
4. Exibe os resultados, incluindo a solução, o número de conflitos, e o tempo de execução.
5. Plota o tabuleiro final se a opção estiver habilitada.

## Requisitos

- Python 3.8 ou superior
- Bibliotecas:
  - `random` (nativa do Python)
  - `time` (nativa do Python)
  - `plot_tabuleiro` (para visualização, deve estar implementada separadamente e localizada na mesma pasta que o arquivo `n_rainhas.py`)

## Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/hugocesarleal/N-Queens.git
   cd N-Rainhas
   ```
2. Certifique-se de que o arquivo `plotar_tabuleiro.py` está na mesma pasta que o arquivo `n_rainhas.py`.
3. Execute o código:
   ```bash
   python n_rainhas.py
   ```

## Parâmetros

- `n`: Número de rainhas (e tamanho do tabuleiro).
- `iteracoesMax`: Número máximo de iterações permitidas.
- `rodarAteEncontrarZero`: Se verdadeiro, o algoritmo continua até encontrar uma solução sem conflitos, independentemente do número de iterações.
- `plotarTabuleiro`: Se verdadeiro, plota o tabuleiro final.

## Resultados

A saída do programa inclui:
- A solução encontrada (disposição das rainhas no tabuleiro).
- O número de conflitos restantes (idealmente 0).
- O número de vizinhos gerados durante a execução.
- O tempo total de execução.

## Exemplo de Saída

```text
Solução:  [1, 3, 5, 2, 4]
Número de rainhas:  5
Fitness:  0
Vizinhos gerados:  17
Tempo de execução: 0.0048732758 segundos
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorias no código ou na documentação.

**Nota**: Este repositório faz parte de um projeto acadêmico e foi desenvolvido para fins educacionais.
