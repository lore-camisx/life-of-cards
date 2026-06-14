import random

def jogada_automatica(jogador):

    if jogador.esta_ativo():
        oponente_jogada = random.randint(0, (len(jogador.mao)-1))
        carta_jogada = jogador.jogar_carta(oponente_jogada)
        return carta_jogada
    return None

    


