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

print(list_num)    
