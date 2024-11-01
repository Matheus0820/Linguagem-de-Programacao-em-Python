# Função
def Digitos(num): 
    if num//10 != 0:
        return str(num%10) + Digitos(num//10)
    else:
        return str(num)


num = int(input())
print(f'Impressao em ordem inversa: {Digitos(num)}')