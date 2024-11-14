# Função
def ContarImpares(num):
    if num//10 != 0:
        if (num%10)%2 != 0:
            return 1 + ContarImpares(num//10)
        else:
            return ContarImpares(num//10)
    else:
        if num%2 != 0:
            return 1
        else:
            return 0

# Resto Código
num = int(input())

print(f"{num} possui {ContarImpares(num)} digitos impares")
