import pygame

def tratar_eventos():
    rodando = True
    pos_mouse = None
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            pos_mouse = evento.pos
            
    return rodando, pos_mouse