N = int(input())
L1 = []

for i in range(N):
    L1.append(input())

x = int(input())
y = int(input())

for i in range(0, N, 1):
    print(i)
    print(L1.__len__)
    comprimento = 0
    for elemento in L1[i]:
        comprimento += 1
    
    if comprimento == x or comprimento == y: 
        L1.remove(L1[i])

print(L1)