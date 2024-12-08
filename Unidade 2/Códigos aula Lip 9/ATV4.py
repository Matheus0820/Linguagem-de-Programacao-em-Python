# Função
def numero_freqeunte(lista1, lista2, lista3, x):
    quantas_lista_aparece = 0

    for i in range(len(lista1)):
        if lista1[i] == x:
            quantas_lista_aparece += 1
            break
    
    for i in range(len(lista2)):
        if lista2[i] == x:
            quantas_lista_aparece += 1
            break
    
    for i in range(len(lista3)):
        if lista3[i] == x:
            quantas_lista_aparece += 1
            break
    
    if quantas_lista_aparece == 2: 
        return True
    else: 
        return False

# Código de teste
lista1 = list(map(int, input().split()))
lista2 = list(map(int, input().split()))
lista3 = list(map(int, input().split()))
x = int(input())

if numero_freqeunte(lista1, lista2, lista3, x):
    print(f"{x} é um número frequente")
else:
    print(f"{x} não é um número frequente")