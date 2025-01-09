# Importações
import numpy as np

# Função
def soma_triangulo_inferior(matriz):
    soma_triango_inferior = 0

    for i in range(matriz.shape):
        for j in range(i, matriz.shape):
            soma_triango_inferior += matriz[j][i]
    
    return soma_triango_inferior

# Código de teste
semente = int(input())
ordem = int(input())

np.random.seed(semente)

matriz = np.zeros(ordem)
print(matriz)

for i in range(ordem):
    lista = np.random.randint(low=1, high=10, size= ordem)
    
    matriz[i] = lista

print("Matriz gerada:")
print(*matriz)
print(f"soma: {soma_triangulo_inferior(matriz)}")

