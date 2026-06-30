import random
from src.carta import Carta


def criar_baralho():
    """Função que monta o baralho do zero."""
    baralho = []

    for valor in Carta.VALORES:
        for naipe in Carta.NAIPES:
            carta = Carta(valor, naipe)
            baralho.append(carta)

    random.shuffle(baralho)
    return baralho


def listar_baralho(baralho):
    """Lista todas as cartas do baralho."""
    for carta in baralho:
        print(carta.valor, "de", carta.naipe)


def distribuir_cartas(baralho, jogadores, quantidade):
    """
    Distribui cartas do baralho para os jogadores.
    
    """
    for jogador in jogadores:
        for _ in range(quantidade):
            if baralho:
                carta = baralho.pop(0)
                jogador.receber_carta(carta)

    return baralho, jogadores