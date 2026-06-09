"""Teste de integração: distribuição de cartas e renderização visual."""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pygame
from src.baralho import criar_baralho, distribuir_cartas
from src.jogador import criar_jogadores
from src.interface import atualizar_display
from src.config import LARGURA_TELA, ALTURA_TELA


def test_integracao_completa():
    """Testa fluxo completo: criar jogadores, distribuir cartas e renderizar."""
    pygame.init()
    pygame.display.set_mode((100, 100))
    
    tela = pygame.Surface((LARGURA_TELA, ALTURA_TELA))
    
    try:
        # Cria jogadores
        jogadores = criar_jogadores()
        assert len(jogadores) == 4
        
        # Cria e distribui baralho
        baralho = criar_baralho()
        baralho, jogadores = distribuir_cartas(baralho, jogadores, 5)
        
        # Verifica se todos têm 5 cartas
        for jogador in jogadores:
            assert jogador.tamanho_mao() == 5, f"{jogador.nome} tem {jogador.tamanho_mao()} cartas"
        
        # Testa renderização
        mesa = []
        rects = []
        
        rects = atualizar_display(tela, jogadores, mesa, rects)
        
        # Deve ter retornado os retângulos do jogador 1
        assert len(rects) == 5
        
        print("✓ Integração completa: 5 cartas por jogador")
        
    finally:
        pygame.quit()


def test_integracao_diferentes_quantidades():
    """Testa com diferentes quantidades de cartas."""
    pygame.init()
    pygame.display.set_mode((100, 100))
    
    tela = pygame.Surface((LARGURA_TELA, ALTURA_TELA))
    
    try:
        quantidades = [1, 2, 3, 4, 5]
        
        for qtd in quantidades:
            jogadores = criar_jogadores()
            baralho = criar_baralho()
            baralho, jogadores = distribuir_cartas(baralho, jogadores, qtd)
            
            # Verifica distribuição
            for jogador in jogadores:
                assert jogador.tamanho_mao() == qtd
            
            # Testa renderização
            mesa = []
            rects = []
            rects = atualizar_display(tela, jogadores, mesa, rects)
            
            assert len(rects) == qtd
        
        print("✓ Integração com 1, 2, 3, 4 e 5 cartas")
        
    finally:
        pygame.quit()


def test_jogada_e_renderizacao():
    """Testa jogar uma carta e atualizar renderização."""
    pygame.init()
    pygame.display.set_mode((100, 100))
    
    tela = pygame.Surface((LARGURA_TELA, ALTURA_TELA))
    
    try:
        jogadores = criar_jogadores()
        baralho = criar_baralho()
        baralho, jogadores = distribuir_cartas(baralho, jogadores, 3)
        
        jogador_1 = jogadores[0]
        
        # Antes de jogar
        assert jogador_1.tamanho_mao() == 3
        
        # Joga uma carta
        carta = jogador_1.jogar_carta(0)
        assert carta is not None
        assert jogador_1.tamanho_mao() == 2
        
        # Renderiza após jogada
        mesa = [carta]
        rects = []
        rects = atualizar_display(tela, jogadores, mesa, rects)
        
        # Deve ter 2 cartas agora (remova a que foi jogada)
        assert len(rects) == 2
        
        print("✓ Jogada e renderização atualizada")
        
    finally:
        pygame.quit()


def test_perder_vida_e_renderizacao():
    """Testa perder vida e continuar renderizando."""
    pygame.init()
    pygame.display.set_mode((100, 100))
    
    tela = pygame.Surface((LARGURA_TELA, ALTURA_TELA))
    
    try:
        jogadores = criar_jogadores()
        baralho = criar_baralho()
        baralho, jogadores = distribuir_cartas(baralho, jogadores, 3)
        
        jogador_1 = jogadores[0]
        
        # Antes de perder vida
        assert jogador_1.vidas == 3
        assert jogador_1.esta_ativo()
        
        # Perde vida
        jogador_1.perder_vida(2)
        assert jogador_1.vidas == 1
        assert jogador_1.esta_ativo()
        
        # Renderiza
        rects = atualizar_display(tela, jogadores, [], [])
        assert len(rects) == 3
        
        # Perde mais uma vida (eliminação)
        jogador_1.perder_vida(1)
        assert jogador_1.vidas == 0
        assert not jogador_1.esta_ativo()
        
        # Renderiza mesmo com jogador eliminado (cartas ainda são exibidas visualmente)
        rects = atualizar_display(tela, jogadores, [], [])
        assert len(rects) == 3  # Cartas continuam visíveis na tela
        
        print("✓ Perder vida e renderização")
        
    finally:
        pygame.quit()


def test_mesa_com_cartas():
    """Testa renderização de cartas na mesa."""
    pygame.init()
    pygame.display.set_mode((100, 100))
    
    tela = pygame.Surface((LARGURA_TELA, ALTURA_TELA))
    
    try:
        jogadores = criar_jogadores()
        baralho = criar_baralho()
        baralho, jogadores = distribuir_cartas(baralho, jogadores, 3)
        
        # Joga 2 cartas na mesa
        carta1 = jogadores[0].jogar_carta(0)
        carta2 = jogadores[1].mao.pop(0)
        mesa = [carta1, carta2]
        
        # Renderiza com mesa
        rects = atualizar_display(tela, jogadores, mesa, [])
        
        # Deve funcionar sem erro
        assert len(rects) == 2  # jogador 1 tem 2 cartas restantes
        
        print("✓ Renderização com mesa")
        
    finally:
        pygame.quit()


if __name__ == "__main__":
    print("\n=== Testes de Integração: Distribuição e Renderização ===\n")
    
    test_integracao_completa()
    test_integracao_diferentes_quantidades()
    test_jogada_e_renderizacao()
    test_perder_vida_e_renderizacao()
    test_mesa_com_cartas()
    
    print("\n=== Todos os testes de integração passaram! ===\n")
