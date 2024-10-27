"""Recebe um número Inteiro e retorna a quantidade de fatores primos que o decompoem"""

# Função
def Decomposicao(num):
    listFatoresPrimos = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    quantFatores = 0
    fator = 0
    
    while num != 1:
        if num % listFatoresPrimos[fator] == 0:
            num = num / listFatoresPrimos[fator]
            quantFatores += 1
        else:
            fator += 1
    
    return quantFatores

# Resto do código
num = int(input())

print(f"{num} tem {Decomposicao(num)} fatores primos")