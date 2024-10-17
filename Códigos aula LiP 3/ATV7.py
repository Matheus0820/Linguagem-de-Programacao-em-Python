# Três números em ordem crescente - Sem usar laços de repetições, listas (arrays) ou funções de bibliotecas 

num1 = int(input())
num2 = int(input())
num3 = int(input())
aux = None

# Checa se num2 ou num3 é maior que num1 e define num1 como o maior - Maior
if num1 < num2:
    aux = num1
    num1 = num2
    num2 = aux

if num1 < num3:
    aux = num1
    num1 = num3
    num3 = aux

# Checa se num3 é maior que num2 e define num2 como o maior - Intemediário 
if num2 < num3:
    aux = num2
    num2 = num3
    num3 = aux

# num3 será o menor valor - Menor

# Exibi resultado
print(num3, num2, num1)