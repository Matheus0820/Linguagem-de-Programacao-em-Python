"""Recebe uma sequência númerica inteira de 10 número e verifica qual é o maior, o menor e faz o MDC do menor e maior"""

# Variáveis de apoio
maior = -10000000000
menor = 10000000000
mdc = 1

# Vai de 0 a 10 e ler os números e verifica qual é o maior e o menor 
for i in range(0, 10):
    num = int(input()) # Ler número

    if num > maior: # Verifica se o numero digitado é maior que o valor da variável maior
        maior = num # Define o valor da variável maior como sendo o número recebido
    
    if num < menor: # Verifica se o numero digitado é menor que o valor da variável maior
        menor = num # Define o valor da variável menor como sendo o número recebido

# Vai de 1 a menor para verificar o MDC
for i in range(1, menor):
    if maior%i == 0 and menor%i == 0: # Verifica se maior e menor é divisivel por i
        mdc *= i # Multiplica o valor da variável mdc pelo valor de i caso ele seja divisor de maior e menor

# Mostra o maior, menor e o mdc
print(maior, menor, mdc)
