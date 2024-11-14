"""Recebe um número inteiro e retorna os digitos e a quantidade de vezes que eles se repetem"""

# Função
def QuantidadeDigitos(num):
    num = str(num)

    for digit in num:
        quant_digit = 0
        for checkDigit in num:
            if digit == checkDigit:
                quant_digit += 1
        
        if quant_digit != 0:
            print(f"{digit} = {quant_digit}")

        num = num.replace(digit, "")

# Resto do código
num = int(input())
QuantidadeDigitos(num)