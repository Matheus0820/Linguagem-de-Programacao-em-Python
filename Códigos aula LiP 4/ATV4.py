"""
Cálculo da constante e, que é igual a soma de 1 mais o somatório de 1 dividido pelo faotorial de 1 até N
"""

N = int(input())
e = 1
fat = None

for i in range(1, N+1):
    fat = 1
    for j in range (1, i+1):
        fat = fat*j

    e += 1/(fat)

print(e)