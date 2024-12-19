# Função
def nova_pizza(lista, x):
    new_lista = []
    for i in range(len(lista)):
        if len(lista[i]) %2 == 0 or len(lista[i]) >= x:
            new_lista.append(lista[i])
    
    return new_lista


# Código de teste
lista = []
N = int(input())
x = int(input())

for i in range(N):
    lista.append(input())

print(f"Pizza original: {lista}")
print(f"Nova pizza: {nova_pizza(lista, x)}")
