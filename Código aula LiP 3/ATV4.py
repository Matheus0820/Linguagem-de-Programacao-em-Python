nota = float(input())
faltas = int(input())

# Aprovado
if (nota >= 5 and faltas <= 20) or nota >= 7:
    print('Aprovado')

# Recuperação
elif nota >= 3 and faltas <= 20:
    print('Recuperação')

# Reprovado
else:
    print('Reprovado')
