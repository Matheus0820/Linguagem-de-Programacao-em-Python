# Funções
def criar_partida(mandante, visitante, gols_mandante, gols_visitente):
    nova_partida = {}

    nova_partida["mandante"] = mandante
    nova_partida["visitante"] = visitante
    nova_partida["gols_mandante"] = gols_mandante
    nova_partida["gols_visitente"] = gols_visitente

    return nova_partida

def calcula_pontos(partidas, time):
    pass