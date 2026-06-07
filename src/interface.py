import pygame
from src.config import PRETO

def desenhar_tela(tela):
    tela.fill(PRETO)

def qual_carta_clicada(pos_mouse, rects_cartas):
    if not pos_mouse:
        return None
        
    for i, retangulo in enumerate(rects_cartas):
        if retangulo.collidepoint(pos_mouse):
            return i
            
    return None