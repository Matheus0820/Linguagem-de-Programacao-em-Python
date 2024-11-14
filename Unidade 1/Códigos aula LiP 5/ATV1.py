"""
Calcula teto de n valores informado pelo usuário sem usando função própria
"""
# Variáveis
diferenca = 0
teto = 0
tetos_calculados = []

# Função responsável por calcular o teto
def calculaTeto(num):
    diferenca = num - int(num) # Pega a diferença do número com sua parte inteira

    if diferenca > 0: # Verifica se a parte inteira é maior que 0, caso sim ele arredonda para cima
       return (int(num) + 1)
    else:
        return int(num)

# Resto do cógido
n = int(input()) # Pega o valor de N

for i in range(0, n): # Laço que vai de 0 até n 
    num = float(input()) # Pega os N valores digitados pelo usuário

    tetos_calculados.append(calculaTeto(num)) # Guarda valores em u em um array

# Mostra valores
print(*tetos_calculados)
