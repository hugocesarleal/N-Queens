import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def desenharTabuleiro(solucao, n):
    caminhoImagem = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rainha.png')  

    fig, ax = plt.subplots()

    tabuleiro = [[(i + j) % 2 for i in range(n)] for j in range(n)]

    ax.imshow(tabuleiro, cmap='gray', extent=[0, n, 0, n])

    imgRainha = mpimg.imread(caminhoImagem)

    for linha in range(n):
        coluna = solucao[linha] - 1
        ax.imshow(imgRainha, extent=[coluna, coluna + 1, n - linha - 1, n - linha], zorder=1)

    ax.set_xticks(range(n))
    ax.set_yticks(range(n))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_xlim(0, n)
    ax.set_ylim(0, n)
    ax.grid(False)
    plt.title(f'Solução para {n} rainhas')
    plt.show()