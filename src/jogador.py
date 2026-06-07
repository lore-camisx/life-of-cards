def criar_jogador(nome):
    jogador = {}
    jogador["nome"] = nome
    jogador["mao"] = []
    return jogador

def criar_jogadores():
    jogadores = []
    nomes = ["Jogador 01", "Jogador 02", "Jogador 03", "Jogador 04"]

    for nome in nomes:
        jogador = criar_jogador(nome)
        jogadores.append(jogador)

    return jogadores

def jogar_carta(jogador, indice):
    if 0 <= indice < len(jogador["mao"]):
        return jogador["mao"].pop(indice)
    return None