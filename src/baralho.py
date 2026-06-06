import random
from src.carta import (criacao_cartas)
from src.jogador import (criar_jogadores)

def criar_baralho(): #Função que monta o baralho do zero

    baralho = [] #Cria uma lista vazia para guardar o baralho 

    naipes = ["Paus", "Copas", "Espadas", "Ouros"] #Define os valores dos naipes
    valores = ["A", 2, 3, 4, 5, 6, 7] #Define os valores das cartas

    for valor in valores: #Percorre cada valor da lista e, a cada volta, valor guarda um elemento da lista
        for naipe in naipes: #para cada valor, percorre todos os naipes (roda 4 vezes para cada valor)
            carta = criacao_cartas(valor, naipe) #Chama a função e cria uma carta
            baralho.append(carta) #Adiciona a carta no baralho 

    random.shuffle(baralho) #Embaralha o baralho de forma aleatória
    
    return baralho #retorna o baralho com as 28 cartas embaralhadas 

def listar_baralho(baralho):

    for carta in baralho: #Percorre cada carta do baralho 
        print(carta["valor"], "de", carta["naipe"]) #Imprime o valor e naipe de cada carta 

def distribuir_cartas(baralho, jogadores, quantidade): #Função que distribui as cartas dos jogadores
    for jogador in jogadores: #Percorre cada jogador da lista
        for i in range(quantidade): #Para cada jogador, repete 5 (quantidade) vezes, sendo uma carta distribuida por vez  
            if (baralho[0]): #Acha a primeira carta do baralho
                jogador["mao"].append(baralho[0]) #Guarda na mão do jogador
                
            novo_baralho = [] #Cria um novo baralho 
        
            for i in range(len(baralho)): #Percorre o baralho
                if (i != 0):
                    novo_baralho.append(baralho[i]) #Adiciona todas cartas no baralho exceto aquela guarada anteriormente 
            
            baralho = novo_baralho #Atualiza o baralho 

    return baralho, jogadores #Retorna o baralho atualizado e os jogadores com as mãos preenchidas
