n = int(input())
valorAnt = None
list_num = []

for i in range(n):
    atualvalor = int(input())
    aux = 0
    if len(list_num) == 0:
        list_num.append(atualvalor)
    else:
        if list_num[i-1] < atualvalor:
            list_num.append(atualvalor)
        else:
            aux = list_num[i-1]
            list_num[i-1] = atualvalor
            list_num.append(aux)

        for j in range(len(list_num)):
            for k in range(len(list_num) - 1):
                if list_num[j] < list_num[k]:
                    aux = list_num[j]
                    list_num[j] = list_num[k]
                    list_num[k] = aux

if len(list_num)%2 != 0:
    idc = int(len(list_num)/2)
    print(f"idc: {idc}")
    mediana = list_num[idc]
else:
    idc1 = int(len(list_num)/2) - 1
    idc2 = idc1 + 1
    mediana = (list_num[idc1] + list_num[idc2])/2
    
print(*list_num)
print(f"Mediana: {mediana:.2f}")    
