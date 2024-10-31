# Função
def Produto(num1, num2):
    if num2 == 0:
        return 0
    else:
        return num1 + Produto(num1, num2-1)


# Resto do código
num1 = int(input())
num2 = int(input())

print(f'Produto entre {num1} e {num2}: {Produto(num1, num2)}')
