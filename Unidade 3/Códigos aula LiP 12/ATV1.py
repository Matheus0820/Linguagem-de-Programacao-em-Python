# Importações
import numpy as np

# Função
def soma_triangulo_inferior(matriz):
    soma_triango_inferior = 0

    for i in range(matriz.shape[0]):
        for j in range(i+1, matriz.shape[0]):
            soma_triango_inferior += matriz[j][i]
    
    return soma_triango_inferior

# Código de teste
semente = int(input())
ordem = int(input())

np.random.seed(semente)

matriz = np.empty(ordem, dtype=object)

print("Matriz gerada:")

for i in range(ordem):
    lista = np.random.randint(low=1, high=10, size= ordem)
    
    print(*lista, end=" ")
    print("")
    matriz[i] = lista

print(f"Soma abaixo da diagonal principal: {soma_triangulo_inferior(matriz)}")