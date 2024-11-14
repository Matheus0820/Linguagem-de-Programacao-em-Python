"""Recebe o número inteiro e retorna a soma dos seus digitos"""

# Variáveis de suporte
soma = 0

# Ler valor como String
numIn = input()

# Separando digitos de numIn
for digit in numIn: # Percorre cada carctere da String da variável numIn
    soma += int(digit) # Soma ao valor da variável soma o valor da variável digit convertido para inteiro

# Mostrar resultado
print(f"A soma dos dígitos de {numIn} = {soma}")