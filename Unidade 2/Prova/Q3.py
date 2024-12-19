# Código
n = int(input())
soma_listaA = 0
for i in range(n):
    if i % 2 != 0:
        soma_listaA += float(input())
    else:
        input()

soma_listaB = 0
for i in range(n):
    if i % 2 == 0:
        soma_listaB += float(input())
    else:
        input()
    
print(f"Resultado: {soma_listaA - soma_listaB:.2f}")