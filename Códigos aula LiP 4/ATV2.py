"""
Decomposição em fatores primos de um número
"""

num = int(input())
divisor = 2

if num > 1: 
    while num != 1:
        if num%divisor == 0:
            num = num/divisor
            print(divisor)
        else: 
            divisor += 1

else: 
    print(1)
