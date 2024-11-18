N = int(input())
L1 = []

for i in range(N):
    L1.append(input())

x = int(input())
y = int(input())

for i in range(N-1, -1, -1):
    comprimento = 0
    for elementos in L1[i]:
        comprimento += 1
    
    if comprimento == x or comprimento == y: 
        L1.remove(L1[i])

print(L1)