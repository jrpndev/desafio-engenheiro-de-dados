
def verifica_par(array):
    return len(array) % 2 == 0

def encontrar_mediana(matriz):
    matriz_ordenada = sorted(matriz)
    if verifica_par(matriz_ordenada):
        meio_esquerda = matriz_ordenada[len(matriz_ordenada) // 2 - 1]
        meio_direita = matriz_ordenada[len(matriz_ordenada) // 2]
        return (meio_esquerda + meio_direita) / 2
    else:
        print(matriz_ordenada)
        return matriz_ordenada[len(matriz_ordenada) // 2]  
    
def encontrar_mediana_duas_matrizes(matrizA, matrizB):
    matriz_resultante = matrizA + matrizB
    matriz_ordenada = sorted(matriz_resultante)
    return encontrar_mediana(matriz_ordenada)

def esta_seguro(tabuleiro, linha, coluna, n):
    for i in range(linha):
        if tabuleiro[i][coluna] == 1:
            return False
    
    i, j = linha, coluna
    while i >= 0 and j >= 0:
        if tabuleiro[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
    i, j = linha, coluna
    while i >= 0 and j < n:
        if tabuleiro[i][j] == 1:
            return False
        i -= 1
        j += 1
    
    return True

def resolver(tabuleiro, linha, n):
    if linha == n:
        return 1
    count = 0
    for coluna in range(n):
        if esta_seguro(tabuleiro, linha, coluna, n):
            tabuleiro[linha][coluna] = 1
            count += resolver(tabuleiro, linha + 1, n)
            tabuleiro[linha][coluna] = 0
    
    return count

def resolver_n_rainhas(n):
    tabuleiro = [[0] * n for _ in range(n)]
    return resolver(tabuleiro, 0, n)



