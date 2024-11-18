N = int(input())
list_name = []

for i in range(N):
    list_name.append(input())

while len(list_name) > 1:
    menor = None
    maior = None
    for i in range(len(list_name)):
        if i%2 == 0 and len(list_name) > 2: # Passos impares
            if maior == None:
                maior = list_name[i]
            elif len(maior) < len(list_name[i]):
                maior = list_name[i]

        elif len(list_name) != 3: # Passos pares
            # print(f"Tamanho: {len(list_name)}")
            if menor == None:
                menor = list_name[i]
            elif len(menor) > len(list_name[i]):
                menor = list_name[i]
    
    # print(f"lista: {list_name} - maior: {maior} - menor: {menor}")
    if maior != None:
        list_name.remove(maior)
    if menor != None:
        list_name.remove(menor)

print(*list_name)