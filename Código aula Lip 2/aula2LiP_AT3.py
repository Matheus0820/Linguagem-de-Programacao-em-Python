numCarta = int(input())

if numCarta >= 0 and numCarta <= 12: 
    print(f"Valor: {numCarta%13}, naipe: 0")

elif numCarta <= 25:
    print(f"Valor: {numCarta%13}, naipe: 1")

elif numCarta <= 38:
    print(f"Valor: {numCarta%13}, naipe: 2")

else:
    print(f"Valor: {numCarta%13}, naipe: 3")