# Funções
def quantdade_de_palavras(string):
    string = string.split()
    quantidade_palavras = len(string)

    return quantidade_palavras

# Código de teste
texto = input()

print(f"{quantdade_de_palavras(texto)} palavras")