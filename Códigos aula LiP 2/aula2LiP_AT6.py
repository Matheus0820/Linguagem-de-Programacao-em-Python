venda = float(input())
valorRecebido = float(input())

troco = valorRecebido - venda
listTroco = [0]*8

def calculaTroco(troco):
    if troco >= 20: 
        listTroco[0] += 1
        calculaTroco(round(troco - 20, 2))

    elif troco >= 10:
        listTroco[1] += 1
        calculaTroco(round(troco - 10, 2))

    elif troco >= 5:
        listTroco[2] += 1
        calculaTroco(round(troco - 5, 2))

    elif troco >= 2:
        listTroco[3] += 1
        calculaTroco(round(troco - 2, 2))

    elif troco >= 1:
        listTroco[4] += 1
        calculaTroco(round(troco - 1, 2))

    elif troco >= 0.5:
        listTroco[5] += 1
        calculaTroco(round(troco - 0.5, 2))

    elif troco >= 0.1:
        listTroco[6] += 1
        calculaTroco(round(troco - 0.1, 2))

    elif troco >= 0.05:
        listTroco[7] += 1
        calculaTroco(round(troco - 0.05, 2))

    else: 
        pass

if troco > 0:
    calculaTroco(troco)
else:
    listTroco.append(0)

retorno = f"""
Venda: R$ {venda}
Troco: R$ {troco:.2f}
Para fazer o troco, entregue:
R$ 20,00 x {listTroco[0]}
R$ 10,00 x {listTroco[1]}
R$ 5,00 x {listTroco[2]}
R$ 2,00 x {listTroco[3]}
R$ 1,00 x {listTroco[4]}
R$ 0,50 x {listTroco[5]}
R$ 0,10 x {listTroco[6]}
R$ 0,05 x {listTroco[7]}
"""

print(retorno)