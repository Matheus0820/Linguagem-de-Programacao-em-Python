idade = int(input())
ocupacao = input()

# Entrada gratuita
if idade < 10 or idade > 70:
    print("Ingresso gratuito")

# Meia entrada
elif (idade < 30 and ocupacao == 'estudante') or ocupacao == 'professor':
    print("Ingresso com desconto")

# Inteira
else:
    print("Ingresso normal")