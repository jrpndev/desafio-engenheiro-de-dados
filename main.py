from functions import encontrar_mediana_duas_matrizes, resolver_n_rainhas

def main():
    matrizA = [9, 11, 16, 7, 2]
    matrizB = [1, 2, 3, 4, 5, 6]
    mediana = encontrar_mediana_duas_matrizes(matrizA, matrizB)
    print("Mediana das duas matrizes classificadas de mesmo tamanho:")
    print(mediana)

    n = 8  # Tamanho do tabuleiro de xadrez (8x8 neste caso)
    solucoes = resolver_n_rainhas(n)
    print(f"Número de soluções distintas para o quebra-cabeça das {n}-rainhas: {solucoes}")

if __name__ == "__main__":
    main()
