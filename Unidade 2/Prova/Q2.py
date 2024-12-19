# Função
def numeros_deficientes(x, y):
    lista_deficientes = []
    while(x <= y):
        soma_divisores = 0
        for i in range(1, x):
            if x % i == 0:
                soma_divisores += i
        
        if soma_divisores < x:
            print(f"{x} e deficiente")

        x += 1
    
    return lista_deficientes

# Código de teste
a = int(input())
b = int(input())

lista_deficientes = numeros_deficientes(a, b)

