# Função
def checa_guloseimas(string, lista_guloseimas):
    lista_string = string.split()

    for i in range(len(lista_string)):
        new_string = ""
        for j in range(len(lista_string[i])):
            if lista_string[i][j] != ",":
                new_string += lista_string[i][j]

        lista_string[i] = new_string
        
 
    quant_guloseimas = 0

    for i in range(len(lista_guloseimas)):
        for j in range(len(lista_string)):
            if lista_string[j] == lista_guloseimas[i]:
                quant_guloseimas += 1
    
    return quant_guloseimas

# Código de teste
texto = input("")
n = int(input())
lista = []

for i in range(n):
    lista.append(input())

print(f"{checa_guloseimas(texto, lista)} guloseima(s) da lista aparece(m) na frase")
