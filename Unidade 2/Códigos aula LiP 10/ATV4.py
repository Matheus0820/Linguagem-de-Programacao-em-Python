# Funções
def verifica_nomes_iguais(nome1, nome2):
    for i in range(len(nome1)):
        if nome1[i] != nome2[i]:
            if (chr(ord(nome1[i]) + 32) == nome2[i]) or (chr(ord(nome1[i]) - 32) == nome2[i]): # Quase Iguais
                return "Quase iguais"
            else: # Difetentes
                return "Nomes diferentes"
            
    return "Nomes iguais" # Se o for acabar as palavras são iguais

# Código de teste
nome1 = input()
nome2 = input()

print(verifica_nomes_iguais(nome1, nome2))