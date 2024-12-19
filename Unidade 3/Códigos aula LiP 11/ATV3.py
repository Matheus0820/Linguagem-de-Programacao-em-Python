# Funções
def criar_prato(nome, valor):
    novo_prato = {}

    novo_prato["nome"] = nome
    novo_prato["valor"] = valor

    return novo_prato

def encotra_pratos_no_orcamento(pratos, valor_max):
    lista_indices_pratos = []

    for i in range(len(pratos)):
        if pratos[i]["valor"] <= valor_max:
            lista_indices_pratos.append(i)
    
    return lista_indices_pratos

# Código de teste
cardapio = []
n = int(input())

for i in range(n):
    nome = input()
    preco = int(input())

    cardapio.append(criar_prato(nome, preco))

valor_maximo_a_pagar = float(input())

indices_pratos_acessiveis = encotra_pratos_no_orcamento(cardapio, valor_maximo_a_pagar)

print("Pratos dentro do orçamento")
for i in range(len(indices_pratos_acessiveis)):
    lista_valores = []
    for valor in cardapio[indices_pratos_acessiveis[i]].values():
        lista_valores.append(valor)

    print(*lista_valores)
