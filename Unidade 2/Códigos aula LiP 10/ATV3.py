# Função
def gera_login(lista):
    nova_lista = []

    for i in range(len(lista)):
        nova_lista.append([])
        for j in range(len(lista[i])):
            nova_lista[i].append(lista[i][j])
    
    nova_lista[0][0] = chr(ord(nova_lista[0][0]) + 32)
    nova_lista[len(nova_lista)-1][0] = chr(ord(nova_lista[len(nova_lista)-1][0]) + 32)

    return "".join(nova_lista[0]) + "." + "".join(nova_lista[len(nova_lista)-1])

# Código de teste

print(gera_login(input().split()))