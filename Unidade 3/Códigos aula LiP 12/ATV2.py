# Importação
import numpy as np

# Função
def verifica_pares_triangulo_superior(matriz):
    pares = 0

    for i in range(matriz.shape[0]):
        for j in range(0, i):
            if matriz[j][i]%2 == 0: 
                pares += 1 
    
    return pares

# Código de teste
semente = int(input())
ordem = int(input())

np.random.seed(semente)
matriz = np.random.randint(low=10, high=100, size=(ordem, ordem))

print("Matriz gerada:")
for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        print(matriz[i][j], end=" ")
    
    print("")

print(f"{verifica_pares_triangulo_superior(matriz)} elementos pares acima da diagonal principal")