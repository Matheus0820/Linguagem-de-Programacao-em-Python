# Função
def verifica_a_e_b(a, b):
    menor_de_a = None
    for i in range(len(a)):
        if i == 0:
            menor_de_a = a[i]
        elif a[i] < menor_de_a:
            menor_de_a = a[i]
    
    maior_de_b = None
    for i in range(len(b)):
        if i == 0:
            maior_de_b = b[i]
        elif b[i] > maior_de_b:
            maior_de_b = b[i]
    
    if menor_de_a > maior_de_b:
        return True
    else:
        return False

# Código de teste
m = int(input())
a = []
for i in range(m):
    a.append(float(input()))

n = int(input())
b = []
for i in range(n):
    b.append(float(input()))

print(f'Saída "{verifica_a_e_b(a, b)}"')