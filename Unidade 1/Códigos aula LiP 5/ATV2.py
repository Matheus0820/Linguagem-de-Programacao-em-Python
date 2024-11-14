"""
Calcula a soma dos multiplos de 3 entre um intevelo de números de a á b
"""

# Variáveis 
somaC1 = 0
somaC2 = 0
x1 = 0
x2 = 0
y1 = 0
y2 = 0

# Função
def calculaSomaMultiplos(num1, num2):
    soma = 0

    for i in range(num1, num2+1):
        if i % 3 == 0: 
            soma += i
    
    return soma

# Resto do código
x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())

somaC1 = calculaSomaMultiplos(x1, x2)

somaC2 = calculaSomaMultiplos(y1, y2)

if somaC1 > somaC2:
    print(f"Intervelo {x1}: {x2}")
elif somaC2 > somaC1:
    print(f"Intervelo {y1}: {y2}")
else:
    print(f"Iguais: {somaC1}")