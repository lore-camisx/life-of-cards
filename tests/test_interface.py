"""Testes para a interface de exibição de cartas."""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pygame
from src.interface import (
    desenhar_carta, desenhar_mao_jogador, 
    desenhar_cartas_oponente_topo, desenhar_cartas_oponente_esquerda,
    desenhar_cartas_oponente_direita, qual_carta_clicada
)
from src.jogador import Jogador, criar_jogadores
from src.carta import criacao_cartas
from src.config import LARGURA_TELA, ALTURA_TELA


def test_desenhar_carta_sem_pygame_error():
    """Testa se desenhar_carta não causa erro (sem display)."""
    # Inicializa pygame em modo dummy (sem janela real)
    pygame.init()
    pygame.display.set_mode((100, 100))
    
    # Cria superfície para desenhar
    tela = pygame.Surface((LARGURA_TELA, ALTURA_TELA))
    
    carta = criacao_cartas("A", "Copas")
    
    try:
        rect = desenhar_carta(tela, 10, 10, carta, mostrar_detalhes=True)
        assert rect is not None
        assert rect.x == 10
        assert rect.y == 10
        print("✓ Desenhar carta sem erro")
    finally:
        pygame.quit()


def test_desenhar_mao_jogador_vazia():
    """Testa desenhar mão vazia."""
    pygame.init()
    pygame.display.set_mode((100, 100))
    
    tela = pygame.Surface((LARGURA_TELA, ALTURA_TELA))
    jogador = Jogador("Teste")
    rects = []
    
    try:
        rects = desenhar_mao_jogador(tela, jogador, rects)
        assert len(rects) == 0
        print("✓ Desenhar mão vazia")
    finally:
        pygame.quit()


def test_desenhar_mao_jogador_com_cartas():
    """Testa desenhar mão com cartas."""
    pygame.init()
    pygame.display.set_mode((100, 100))
    
    tela = pygame.Surface((LARGURA_TELA, ALTURA_TELA))
    jogador = Jogador("Teste")
    
    for i in range(3):
        jogador.receber_carta(criacao_cartas("A", "Copas"))
    
    rects = []
    
    try:
        rects = desenhar_mao_jogador(tela, jogador, rects)
        assert len(rects) == 3
        print("✓ Desenhar mão com cartas")
    finally:
        pygame.quit()


def test_qual_carta_clicada_nenhuma():
    """Testa detecção de clique quando nenhuma carta foi clicada."""
    rects = [
        pygame.Rect(10, 10, 60, 90),
        pygame.Rect(80, 10, 60, 90),
    ]
    
    resultado = qual_carta_clicada((200, 200), rects)
    assert resultado is None
    print("✓ Clique fora das cartas")


def test_qual_carta_clicada_primeira():
    """Testa detecção de clique na primeira carta."""
    rects = [
        pygame.Rect(10, 10, 60, 90),
        pygame.Rect(80, 10, 60, 90),
    ]
    
    resultado = qual_carta_clicada((30, 30), rects)
    assert resultado == 0
    print("✓ Clique na primeira carta")


def test_qual_carta_clicada_segunda():
    """Testa detecção de clique na segunda carta."""
    rects = [
        pygame.Rect(10, 10, 60, 90),
        pygame.Rect(80, 10, 60, 90),
    ]
    
    resultado = qual_carta_clicada((100, 50), rects)
    assert resultado == 1
    print("✓ Clique na segunda carta")


def test_qual_carta_clicada_nenhuma_pos():
    """Testa detecção com posição None."""
    rects = [pygame.Rect(10, 10, 60, 90)]
    
    resultado = qual_carta_clicada(None, rects)
    assert resultado is None
    print("✓ Posição None")


def test_desenhar_cartas_oponentes():
    """Testa desenho de cartas dos oponentes."""
    pygame.init()
    pygame.display.set_mode((100, 100))
    
    tela = pygame.Surface((LARGURA_TELA, ALTURA_TELA))
    jogador = Jogador("Oponente")
    
    for i in range(2):
        jogador.receber_carta(criacao_cartas("2", "Espadas"))
    
    try:
        rects_topo = desenhar_cartas_oponente_topo(tela, jogador)
        rects_esq = desenhar_cartas_oponente_esquerda(tela, jogador)
        rects_dir = desenhar_cartas_oponente_direita(tela, jogador)
        
        assert len(rects_topo) == 2
        assert len(rects_esq) == 2
        assert len(rects_dir) == 2
        print("✓ Desenhar cartas dos oponentes")
    finally:
        pygame.quit()


def test_posicionamento_cartas():
    """Testa se cartas não se sobrepõem excessivamente."""
    pygame.init()
    pygame.display.set_mode((100, 100))
    
    tela = pygame.Surface((LARGURA_TELA, ALTURA_TELA))
    jogador = Jogador("Teste")
    
    for i in range(5):
        jogador.receber_carta(criacao_cartas("A", "Copas"))
    
    rects = []
    
    try:
        rects = desenhar_mao_jogador(tela, jogador, rects)
        
        # Verifica se rects não têm sobreposição excessiva
        assert len(rects) == 5
        
        # Verifica espaçamento horizontal
        for i in range(len(rects) - 1):
            distancia = rects[i + 1].x - (rects[i].x + rects[i].width)
            assert distancia == 10, f"Espaçamento inválido: {distancia}"
        
        print("✓ Posicionamento das cartas correto")
    finally:
        pygame.quit()


if __name__ == "__main__":
    print("\n=== Executando testes de Interface ===\n")
    
    test_desenhar_carta_sem_pygame_error()
    test_desenhar_mao_jogador_vazia()
    test_desenhar_mao_jogador_com_cartas()
    test_qual_carta_clicada_nenhuma()
    test_qual_carta_clicada_primeira()
    test_qual_carta_clicada_segunda()
    test_qual_carta_clicada_nenhuma_pos()
    test_desenhar_cartas_oponentes()
    test_posicionamento_cartas()
    
    print("\n=== Todos os testes passaram! ===\n")
