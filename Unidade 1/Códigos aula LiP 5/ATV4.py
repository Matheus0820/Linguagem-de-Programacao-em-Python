"""Calcula a quantidade de número primos entre cada número do conjuto que vai de 1 até um número inteiro N"""

# Função
def pi(x):
    primos = 0 # Quantidade de primos de x

    for i in range(0, x + 1): # Vai de 0 até o número x
        divisores = 0 # Quantidade de divisores de i

        for j in range(1, i+1):  # Vai de 1 até i para saber os divisores de i
            if i % j == 0: # Se i for divisivel por j, j é divisor de i, logo i tem um divisor
                divisores += 1 # Somamos 1 ao valor da variável divisores pois i possui mais 1 divisor
        
        if divisores == 2: # Se divisores for igual 2 indica que i é primo
            primos += 1 # Como i é primo somamos mais 1 na variável primo

    return primos # Retorna a quantidade de primos entre 0 e x

# Resto do código
m = int(input()) # Recebe um valor m inteiro

print("Contagem de primos:")
for i in range(1, m + 1): # Vai de 1 até m
    print(pi(i), end= " ") # Mostra a quantidade de primos que há em i, que é o retorno da função pi
