# Valor Intermediário

num1 = int(input())
num2 = int(input())
num3 = int(input())

# Caso num1 seja o intermediário
if (num1 < num2 and num1 > num3) or (num1 > num2 and num1 < num3):
    print(num1)

# Caso num2 seja o intermediário
elif (num2 < num1 and num2 > num3) or (num2 > num1 and num2 < num3):
    print(num2)

# Caso num3 seja o intermediário
elif (num3 < num1 and num3 > num2) or (num3 > num1 and num3 < num2):
    print(num3)

# Caso não exista intermediário
else:
    print('Nao existe')