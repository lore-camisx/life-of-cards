import pygame

def tratar_eventos():
    """Processa fechamento, tecla ESC e clique esquerdo do mouse."""
    rodando = True
    pos_mouse = None
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                rodando = False

            elif evento.key == pygame.K_r:
                return "reiniciar", None

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                pos_mouse = evento.pos
                    
    return rodando, pos_mouse