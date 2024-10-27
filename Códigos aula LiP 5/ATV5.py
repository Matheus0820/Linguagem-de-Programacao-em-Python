"""Recebe um número inteiro e fala a quantidade de digitos impares e a quantidade de digitos impares consecutivos"""

# Função
def DigitosImpares(numero):
    numero = str(numero)

    quant_impares = 0
    quant_consecultiva = 0
    flag = False
    for digito in numero:
        if int(digito)%2 != 0:
            quant_impares += 1
            if flag == True:
                quant_consecultiva += 1
            flag = True
        else:
            flag = False
    
    return quant_impares, quant_consecultiva

# Resto do código
numero = int(input())

quantImpare, quantConsecultivos = DigitosImpares(numero)

print(f"{numero} possui {DigitosImpares(numero)[0]} digitos impares e {DigitosImpares(numero)[1]} digitos impares consecutivos")