# Importações
import numpy as np
# Funções
def troca_linha(matriz, l, c, a, b):
    for j in range(c):
        aux = matriz[a][j]
        matriz[a][j] = matriz[b][j]
        matriz[b][j] = aux

def mostrar_matriz(matriz):
    for i in range(matriz.shape[0]): 
        for j in range(matriz.shape[1]):
            print(matriz[i][j], end=" ")
        print()

# Resto do Código
semente = int(input())
n_linhas = int(input())
n_colunas = int(input())
a = int(input())
b = int(input())

np.random.seed(semente)
matriz = np.random.randint(low=10, high=100, size=(n_linhas, n_colunas))
print("Matriz gerada:")
mostrar_matriz(matriz)

print("Matriz apos troca:")
troca_linha(matriz, n_linhas, n_colunas, a, b)
mostrar_matriz(matriz)