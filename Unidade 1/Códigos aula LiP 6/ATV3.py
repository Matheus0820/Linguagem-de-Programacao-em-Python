# Função
def Digitos(num): 
    if num//10 != 0:
        return Digitos(num//10) + " " + str(num%10)
    else:
        return str(num)


num = int(input())
print(f'Impressao em ordem: {Digitos(num)}')