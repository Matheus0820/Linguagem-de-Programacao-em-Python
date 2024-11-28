lista_sequencia = input().split()
lista_sequencia = list(map(int, lista_sequencia))

for i in range(len(lista_sequencia)-1, -1, -1):
    vezes_aparece = 1
    elemento = lista_sequencia[len(lista_sequencia)-1]
    for j in range(len(lista_sequencia)-1, len(lista_sequencia) - i, -1):
        if lista_sequencia[j] == elemento:
            vezes_aparece += 1
            del lista_sequencia[j]
    print(f"{elemento} = {vezes_aparece}")
