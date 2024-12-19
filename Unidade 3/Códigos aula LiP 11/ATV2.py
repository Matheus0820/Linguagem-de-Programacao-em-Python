# Funções
def criar_pedido(nome, preco, ingredientes):
    novo_pedido = {}
    
    novo_pedido["nome"] = nome
    novo_pedido["preco"] = preco
    novo_pedido["ingredientes"] = ingredientes

    return novo_pedido

def encontra_pizza_mais_cara(pedidos, ingrediente):
    pizzas_com_ingrediente = []
    maior_preco = 0
    
    for i in range(len(pedidos)):
        if ingrediente in pedidos[i]["ingredientes"]:
            pizzas_com_ingrediente.append(pedidos[i])
            if pedidos[i]["preco"] > maior_preco:
                maior_preco = pedidos[i]["preco"]
    
    if len(pizzas_com_ingrediente) != 0:
        for i in range(len(pizzas_com_ingrediente)):
            if maior_preco == pizzas_com_ingrediente[i]["preco"]:
                print(pizzas_com_ingrediente[i]["nome"])
    else: 
        print(f"Nenhuma pizza tem {ingrediente}")

# Código de teste
pedidos = []
n = int(input())

for i in range(n):
    nome = input()
    preco = float(input())
    ingredientes = input().split()

    pedidos.append(criar_pedido(nome, preco, ingredientes))

ingrediente_x = input()

encontra_pizza_mais_cara(pedidos, ingrediente_x)