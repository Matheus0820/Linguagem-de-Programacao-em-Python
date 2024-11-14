n = int(input())
lista = []
flag = False

for i in range(n):
    lista.append(int(input()))
    if lista[i] < lista[i-1]:
        flag = True
        break

if flag:
    print("ELEMENTOS NÃO ORDENADOS")
else:
    print("ELEMENTOS ORDENADOS")
