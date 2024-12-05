# Função 
def formata_nome(nome):
    i = 0
    nomel =[]
    while(nome[i] == " "):
        i += 1
    
    for j in range(i, len(nome)): 
        nomel.append(nome[j])
    
    if nomel[0] >= 'a' and nomel[0] <= 'z':
        nomel[0] = chr(ord(nomel[0]) - 32)
        
    return "".join(nomel)



# Código para teste
primeiro_nome = formata_nome(input())
segundo_nome = formata_nome(input())

print(primeiro_nome, segundo_nome)