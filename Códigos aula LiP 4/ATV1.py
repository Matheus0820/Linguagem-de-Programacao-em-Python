"""
Fatorial de um número m e seus antecessores até 1
"""
m = int(input())
fat = None

for i in range(1, m+1):
    fat = 1
    for j in range(i, 1, -1): 
        fat = fat*j

    print(f"{i}! = {fat}")