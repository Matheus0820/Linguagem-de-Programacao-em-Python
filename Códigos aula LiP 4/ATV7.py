"""Checar se os digitos de um número inteiro é composto apenas por zeros(0s) e uns(1s)"""
# Variáveis de apoio
flag = False
digit = None

# Ler valor inteiro
num = int(input())

while num > 0: # O lanço continuará até num ser maior que 0
    digit = num % 10 # Pega o ultimo digito utilizando o resto da divisão por 10 -> Ex.: 1001 % 10 = 1
    num = num // 10 # Retira o último número fazendo uma divisão inteira por 10 -> Ex.: 1001 // 10 = 100

    if digit > 1: # Varifica se o digito extraido é maior que um
        flag = True # Define flag como True caso número for maior que 1
        break # Sai do laço de repetição

# Verifica valor booleano da flag e mostra o resultado
if flag:
    print("Numero não é formado apenas por 0s e 1s")
else:
    print("Numero é formado apenas por 0s e 1s")