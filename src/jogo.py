import pygame 

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    PRETO,
)

def executar_jogo(): 

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))  #Cria a tela do jogo 
    pygame.display.set_caption(TITULO_JOGO) #Define o título do jogo
    relogio = pygame.time.Clock() #Objeto que controla o tempo 

    rodando = True #Controla o loop
 
    while rodando: #Roda o loop principal enquanto rodando for "true" 
        
        relogio.tick(FPS) #Limita o FPS 

        for evento in pygame.event.get(): #Coleta o que usuário fez e percorre cada um
            if evento.type == pygame.QUIT: #Evento de "fechar a janela"
                rodando = False #Para o loop 

        tela.fill(PRETO)       #Pinta a tela com a cor preta
        pygame.display.flip()  #Atualiza a janela com tudo que foi desenhado nessa tela 

        