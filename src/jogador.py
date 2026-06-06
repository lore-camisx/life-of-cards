def criar_jogador(nome):
    jogador = {} #Cria um dicionário vazio que representa o jogador

    jogador["nome"] = nome #Preenche o dicionário com o nome do jogador
    jogador["mao"] = [] #Preenche o dicionário com a mão do jogador

    return jogador #Retorna o jogador criado 

def criar_jogadores(): #Função que cria os 4 jogadores 

    jogadores = [] #Cria uma lista vazia para guardar os jogadores criados

    nomes = ["Jogador 01", "Jogador 02", "Jogador 03", "Jogador 04"] #Nomes dos 4 jogadores

    for nome in nomes: #Percorre cada nome da lista 
        jogador = criar_jogador(nome) #Cria um jogador
        jogadores.append(jogador) #Adiciona o jogador criado na lista de jogadores

    return jogadores #Retorna os 4 jogadores criados 
