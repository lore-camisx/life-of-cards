import random
from src.carta import (criacao_cartas)
from src.jogador import (criar_jogadores)

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

def distribuir_cartas(baralho, jogadores, quantidade):
    for jogador in jogadores:
        for i in range(quantidade):
            if (baralho[0]):
                jogador["mao"].append(baralho[0])
                
            novo_baralho = []
        
            for i in range(len(baralho)):
                if (i != 0):
                    novo_baralho.append(baralho[i])
            
            baralho = novo_baralho

    return baralho, jogadores
