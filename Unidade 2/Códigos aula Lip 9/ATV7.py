import math

# Função
def verifica_maior_diferenca(lista):
    maior_diferenca = -1
    valores_diferenca = [0, 0]

    for i in range(len(lista)):
        if i < len(lista) - 1:
            nova_diferenca = math.sqrt((lista[i] - lista[i + 1])**2)

            if nova_diferenca > maior_diferenca:
                maior_diferenca = nova_diferenca
                valores_diferenca[0] = lista[i]
                valores_diferenca[1] = lista[i+1]
    
    return maior_diferenca, valores_diferenca

# Codígo de teste
lista = []
valor_recebido = None
while valor_recebido != 0:
    valor_recebido = int(input())
    lista.append(valor_recebido)

diferenca, vetor_return = verifica_maior_diferenca(lista)

print(f"{vetor_return[0]} e {vetor_return[1]}, cuja subtração em módulo é {int(diferenca)}.")