# Função
def inverte_string(string):
    lista_string = string.split()
    nova_lista_string = []

    for i in range(len(lista_string) - 1, -1, -1):
        nova_lista_string.append(lista_string[i])

    nova_string = " ".join(nova_lista_string)
    return nova_string

# Código de teste
frase = input()
print(f"{inverte_string(frase)}")
        