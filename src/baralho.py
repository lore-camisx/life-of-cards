import random
from src.carta import Carta


def criar_baralho():
    """Função que monta o baralho do zero."""
    baralho = []

    naipes = ["Paus", "Copas", "Espadas", "Ouros"]
    valores = ['A', '2', '3', '4', '5', '6', '7']

    for valor in valores:
        for naipe in naipes:
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

    Compatível com objetos Jogador e dicionários legados.
    """
    for jogador in jogadores:
        for _ in range(quantidade):
            if baralho:
                carta = baralho.pop(0)

                if hasattr(jogador, 'receber_carta'):
                    jogador.receber_carta(carta)
                else:
                    jogador["mao"].append(carta)

    return baralho, jogadores