# Importação
import numpy as np

# Funções
def produto_vetor_coluna(matriz, k):
    produto = 1
    for i in range(matriz.shape[0]):
        produto *= matriz[i][k]
    
    return produto

# Resto do Código
semente = int(input())
l = int(input())
c = int(input())
k = int(input())

np.random.seed(semente)
matriz = np.random.randint(low=1, high=10, size=(l, c))

print("Matriz gerada:")
for i in range(l):
    for j in range(c):
        print(matriz[i][j], end=" ")
    print()

print(f"Produtorio do vetor coluna {k}: {produto_vetor_coluna(matriz, k)}")