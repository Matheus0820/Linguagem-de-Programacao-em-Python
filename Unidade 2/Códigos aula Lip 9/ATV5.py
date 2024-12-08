# Função
def produto_escalar(u, v, index):
    if index == len(u) - 1:
        return u[index] * v[index]
    else:
        return u[index] * v[index] + produto_escalar(u, v, index+1)


# Código de teste
n = int(input())
u = []
for i in range(n):
    u.append(int(input()))

v = []
for i in range(n):
    v.append(int(input()))

print(f"Produto escalar: {produto_escalar(u, v, 0)}")