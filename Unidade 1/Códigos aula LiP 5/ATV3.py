"""Calcula a soma dos números pares menores ou igual a uma entrada N"""

# Função
def somaPares(N):
    soma = 0
    for i in range(0, N+1, 2): # Laço de repetição que começa do 0 e vai até N + 1 incremetando a i de 2 e 2
        soma += i # Soma o valor de i ao valor da variável soma. i sempre será par pois estar somando de 2 e 2

    return soma # Retorna o valor da variável soma

# Resto do código
N = int(input()) # Ler entrada e tranforma em inteiro

print(somaPares(N)) # Exibe o valor de retorno da função SomaPares ao receber o valor N