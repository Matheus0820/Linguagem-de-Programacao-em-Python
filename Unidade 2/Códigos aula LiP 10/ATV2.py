# Função
def verifica_numero_e_letra(string):
    for i in range(len(string)):
        if not ((string[i] >= 'a' and string[i] <= 'z') or (string[i] >= 'A' and string[i] <= 'Z') or (string[i] >= '0' and string[i] <= '9')):
            return 'Chata'
    
    return 'Legal'
        

# Código de teste
print(verifica_numero_e_letra(input()))