# Pedra, Pepel e Tesoura
in1 = input()
in2 = input()

# Situação na qual o jogador 1 vence
if ('r' in in1 and 's' in in2) or ('s' in in1 and 'p' in in2) or ('p' in in1 and 'r' in in2):
    print('Jogador 1 ganhou')

# Caso a entrada do jogador 1 for igual a entrada do jogador 2 é empate
elif in1 == in2: 
    print('Empate')

# Caso o jogador 1 não vença o jogador 2 vence
else:
    print('Jogador 2 ganhou')