# Função
def remove_elemento(lista, index):
    lista.pop(index)

# Código de teste
n = int(input())
lista = []
for i in range(n):
    lista.append(int(input()))

index = int(input())

remove_elemento(lista, index)
if len(lista) > 0:
    print(*lista)
else:
    print("lista vazia")