import pygame 
from src.jogo import executar_jogo


if __name__ == "__main__":
    # Ponto de entrada da aplicação.

    pygame.init()
    executar_jogo()
    pygame.quit()