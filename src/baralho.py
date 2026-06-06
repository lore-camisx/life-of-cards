import random
from src.carta import (criacao_cartas)

def criar_baralho():

    baralho = []

    naipes = ["Paus", "Copas", "Espadas", "Ouros"]
    valores = ["A", 2, 3, 4, 5, 6, 7]

    for valor in valores:
        for naipe in naipes:
            carta = criacao_cartas(valor, naipe)
            baralho.append(carta)

    random.shuffle(baralho)
    
    return baralho

def listar_baralho(baralho):

    for carta in baralho:
        print(carta["valor"], "de", carta["naipe"])

