def criacao_cartas(valor, naipe): #Função que constrõe as cartas
    carta = {} #Cria um dicionário vazio 

    carta["naipe"] = naipe  #Preenche o dicionário com os valores dos naipes
    carta["valor"] = valor  #Preenche o dicionário com os valores das cartas

    return carta #Retorna a carta montada 

