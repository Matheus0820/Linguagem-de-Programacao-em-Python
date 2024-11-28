# Funções
def create_list(N):
    lista_num_pares = []
    for i in range (2, N+1, 2):
        lista_num_pares.append(i)
    
    return lista_num_pares

def soma_pares_lista(lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    
    return soma

# Resto do código
N = int(input())
lista = create_list(N)
print(soma_pares_lista(lista))


