import pygame 
from src.jogo import executar_jogo


if __name__ == "__main__":
    # Ponto de entrada da aplicação.

    pygame.init() #Inicializa o pygame 
    executar_jogo() #Chama a função que executa o jogo
    pygame.quit() #Desliga o pygame 