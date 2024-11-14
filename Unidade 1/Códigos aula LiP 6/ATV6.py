# Função
def s(n):
    if n > 1:
        return n + s(n -1)
    if n == 1:
        return 1

# Resto do Código
n = int(input())

print(s(n))