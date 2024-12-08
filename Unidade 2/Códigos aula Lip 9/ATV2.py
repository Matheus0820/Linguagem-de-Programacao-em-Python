# Funções
# String -> List ordenada de números
def Tranformar_em_lista(string):
    lista = string.split()
    lista = list(map(int, lista))

    return lista

# Conta as repetições dos números na lista
def Contar_repeticoes(lista):
    while len(lista) > 0:
        valor_analisado = lista[0]
        quantidade = 1
        lista_repete = [0]

        for i in range(1, len(lista)):
            if lista[i] == valor_analisado:
                quantidade += 1
                lista_repete.append(i)
        
        print(f"{valor_analisado} = {quantidade}")
        
        for i in range(len(lista_repete)-1, -1, -1):
            del lista[lista_repete[i]]



# Código de teste
lista = Tranformar_em_lista(input())
Contar_repeticoes(lista)