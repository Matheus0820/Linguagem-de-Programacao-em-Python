n = int(input())
lista = []
resposta = 0

for i in range(n):
    lista.append(int(input()))

for i in range(1, len(lista)):
    somaAnteriores = 0

    for j in range(0, i):
        somaAnteriores += lista[j]
    
    if lista[i] > somaAnteriores:
        resposta = i
        break; 

if resposta > 0:
    print(f"dia {resposta}")
else:
    print("não há")