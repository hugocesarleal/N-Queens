import random
import time
from plot_tabuleiro import desenharTabuleiro

def gerarSolucaoInicial(n):
    return random.sample(range(1, n + 1), n)  #vetor com numeros aleatorios sem repetir 

def funcaoObjetivo(solucao):
    diagonalPositiva = set()
    diagonalNegativa = set()
    rainhasComConflito = set()
    
    conflitos = 0

    for i in range(len(solucao)):
        dpK = i - solucao[i] + 1
        dnK = i + solucao[i] + 1
        
        if dpK in diagonalPositiva or dnK in diagonalNegativa:
            conflitos += 1
            rainhasComConflito.add(i)  #adiciona a rainha que esta na linha i aos conflitos
        
        diagonalPositiva.add(dpK)
        diagonalNegativa.add(dnK)
        
    return conflitos, list(rainhasComConflito)

def gerarVizinho(solucao, rainhasConflito):
    n = len(solucao)
    vizinho = solucao[:]

    if rainhasConflito:
        pos1 = random.choice(rainhasConflito)  #escolhe uma rainha que esta causando conflito
        pos2 = random.randrange(n) #escolhe qualquer outra posicao para trocar
        
        while pos1 == pos2: #garante que sao duas posicoes diferentes
            pos2 = random.randrange(n)
            
        vizinho[pos1], vizinho[pos2] = vizinho[pos2], vizinho[pos1] #faz a troca das duas posições
        
    return vizinho

def buscaTabu(n, iteracoesMax, rodarAteEncontrarZero):
    solucaoAtual = gerarSolucaoInicial(n)
    conflitosAtual, rainhasConflito = funcaoObjetivo(solucaoAtual)

    iteracaoAtual = 0
    vizinhosGerados = 0

    melhorSolucao = solucaoAtual[:]
    melhorConflitos = conflitosAtual
    
    if conflitosAtual == 0:
        return melhorSolucao, melhorConflitos, vizinhosGerados
        
    while True:
        vizinho = gerarVizinho(solucaoAtual, rainhasConflito)  #gera um novo vizinho
        conflitosVizinho, rainhasConflitoVizinho = funcaoObjetivo(vizinho)
        
        vizinhosGerados += 1

        if conflitosVizinho < conflitosAtual or (conflitosVizinho == conflitosAtual and random.random() > 0.5):
            solucaoAtual[:] = vizinho[:]
            conflitosAtual = conflitosVizinho
            rainhasConflito = rainhasConflitoVizinho

            if conflitosAtual < melhorConflitos:
                melhorSolucao[:] = solucaoAtual[:]
                melhorConflitos = conflitosAtual

        if melhorConflitos == 0:
            break
        
        if not rodarAteEncontrarZero and iteracaoAtual >= iteracoesMax:
            break
        
        iteracaoAtual += 1

    return melhorSolucao, melhorConflitos, vizinhosGerados

if __name__ == "__main__":
    n = 50
    iteracoesMax = 3000
    rodarAteEncontrarZero = True
    plotarTabuleiro = True

    inicio = time.time()

    solucao, fitness, vizinhosGerados = buscaTabu(n, iteracoesMax, rodarAteEncontrarZero)

    fim = time.time()

    print("Solução: ", solucao)
    print("Número de rainhas: ", n)
    print("Fitness: ", fitness)
    print("Vizinhos gerados: ", vizinhosGerados)
    print(f"Tempo de execução: {fim - inicio:.10f} segundos")
    
    if(plotarTabuleiro):
        desenharTabuleiro(solucao, n)