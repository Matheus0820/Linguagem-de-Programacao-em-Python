"""
Sequência de Fibonacci até um número dado pelo usuário
"""
num = int(input())
termo1 = 0
termo2 = 1
aux = 0
contador = 0

while contador < num:
    if contador <= 1:
        if contador == 0: 
            print(termo1, end=" ")
        else: 
            print(termo2, end=" ")
    else:
        aux = termo2
        termo2 = termo1 + termo2
        termo1 = aux
        print(termo2, end=" ")

    contador += 1