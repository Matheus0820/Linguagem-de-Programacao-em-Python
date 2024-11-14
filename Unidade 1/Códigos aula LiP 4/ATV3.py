"""
Somatório de n elevado a 1/n que começa em n=1 e vai até n=b
"""
b = int(input())
y = 0

for n in range(1, b+1):
    y += n**(1/n)

print(y)