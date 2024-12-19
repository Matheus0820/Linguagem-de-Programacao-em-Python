# Funções
def construtor_musica(nome, estilo):
    nova_musica = {}

    nova_musica["nome"] = nome
    nova_musica["estilo"] = estilo

    return  nova_musica

def encontrar_musicas(musicas, estilos):
    lista_musica_achadas = []
    for i in range(len(musicas)):
        if musicas[i]["estilo"] in estilos:
            lista_musica_achadas.append(musicas[i]["nome"])
    
    return lista_musica_achadas

# Código teste
musicas = []
estilos = []
n = int(input())

for i in range(n):
    nome = input()
    estilo = input()

    musicas.append(construtor_musica(nome, estilo))

m = int(input())

for i in range(m):
    estilos.append(input())

print(*encontrar_musicas(musicas, estilos), sep="\n")

