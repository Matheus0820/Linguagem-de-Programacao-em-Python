# Importações
import numpy as np

# Função
def desloca_para_direita(vetor_input):
    aux = None

    for i in range(vetor_input.shape[0]):
        if i == 0:
            aux = vetor_input[0]
            vetor_input[0] = vetor_input[vetor_input.shape[0]-1]
        else:
            aux2 = vetor_input[i]
            vetor_input[i] = aux
            aux = aux2
    
    return vetor_input

# Código de teste
semente = int(input())
tamanho = int(input())
p = int(input())
q = int(input())

np.random.seed(semente)
vetor = np.random.randint(low=p, high=q, size=tamanho)
print("Vetor gerado:")
print(vetor)

vetor_return = desloca_para_direita(vetor)
print("Vetor apos deslocamento:")
print(vetor_return)