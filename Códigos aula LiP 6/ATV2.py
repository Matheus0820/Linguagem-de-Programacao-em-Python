# Função
def Resto(num1, num2):
    if num1-num2 == 0:
        return 0
    elif num1-num2 < 0:
        return num1
    else:
        return Resto(num1 - num2, num2)
    

# Resto do Código

num1 = int(input())
num2 = int(input())

print(f'Resto da divisao entre {num1} e {num2}: {Resto(num1, num2)}')