# Função
def MaiorDigito(num, maior = 0):
    if num < 0:
        num = num*-1

    if num//10 != 0:
        if num%10 > maior:
            return MaiorDigito(num//10, num%10)
        else:
            return MaiorDigito(num//10, maior)
    else:
        if num > 0:
            if num > maior:
                return num
            else: 
                return maior
        else:
            if num*-1 > maior:
                return num*-1
            else:
                return maior

# Resto do código
num = int(input())

print(f"O maior dígito é {MaiorDigito(num)}")
