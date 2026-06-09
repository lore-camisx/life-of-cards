"""Testes para a estrutura de Jogador."""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.jogador import Jogador, criar_jogador, criar_jogadores
from src.carta import criacao_cartas


def test_criar_jogador_basico():
    """Testa a criação básica de um jogador."""
    jogador = Jogador("Teste Player")
    
    assert jogador.nome == "Teste Player"
    assert jogador.vidas == 3
    assert len(jogador.mao) == 0
    assert jogador.ativo is True
    assert jogador.esta_ativo() is True
    print("✓ Criação básica de jogador")


def test_receber_carta():
    """Testa a adição de cartas à mão do jogador."""
    jogador = Jogador("Player 1")
    carta = criacao_cartas("A", "Copas")
    
    jogador.receber_carta(carta)
    
    assert jogador.tamanho_mao() == 1
    assert jogador.mao[0] == carta
    print("✓ Receber carta")


def test_jogar_carta():
    """Testa a remoção de carta da mão."""
    jogador = Jogador("Player 1")
    carta1 = criacao_cartas("A", "Copas")
    carta2 = criacao_cartas("2", "Espadas")
    
    jogador.receber_carta(carta1)
    jogador.receber_carta(carta2)
    
    assert jogador.tamanho_mao() == 2
    
    carta_jogada = jogador.jogar_carta(0)
    
    assert carta_jogada == carta1
    assert jogador.tamanho_mao() == 1
    assert jogador.carta_jogada == carta1
    print("✓ Jogar carta")


def test_perder_vida():
    """Testa o sistema de perda de vidas."""
    jogador = Jogador("Player 1")
    
    assert jogador.vidas == 3
    assert jogador.ativo is True
    
    jogador.perder_vida()
    
    assert jogador.vidas == 2
    assert jogador.ativo is True
    
    jogador.perder_vida(2)
    
    assert jogador.vidas == 0
    assert jogador.ativo is False
    print("✓ Perder vida")


def test_eliminacao_por_zero_vidas():
    """Testa que jogador com 0 vidas é marcado como eliminado."""
    jogador = Jogador("Player 1")
    
    jogador.perder_vida(3)
    
    assert jogador.vidas == 0
    assert jogador.esta_eliminado() is True
    assert jogador.esta_ativo() is False
    print("✓ Eliminação por zero vidas")


def test_criar_multiplos_jogadores():
    """Testa a criação de múltiplos jogadores."""
    jogadores = criar_jogadores()
    
    assert len(jogadores) == 4
    
    for i, jogador in enumerate(jogadores, 1):
        assert jogador.nome == f"Jogador {i:02d}"
        assert jogador.id == i
        assert jogador.vidas == 3
        assert jogador.esta_ativo() is True
    
    print("✓ Criar múltiplos jogadores")


def test_limpar_carta_jogada():
    """Testa a limpeza da carta jogada."""
    jogador = Jogador("Player 1")
    carta = criacao_cartas("A", "Copas")
    
    jogador.receber_carta(carta)
    jogador.jogar_carta(0)
    
    assert jogador.carta_jogada is not None
    
    jogador.limpar_carta_jogada()
    
    assert jogador.carta_jogada is None
    print("✓ Limpar carta jogada")


def test_get_info():
    """Testa a obtenção de informações do jogador."""
    jogador = Jogador("Player 1", 1)
    carta = criacao_cartas("A", "Copas")
    jogador.receber_carta(carta)
    
    info = jogador.get_info()
    
    assert info["nome"] == "Player 1"
    assert info["id"] == 1
    assert info["vidas"] == 3
    assert info["mao_tamanho"] == 1
    assert info["ativo"] is True
    assert info["eliminado"] is False
    print("✓ Get info")


def test_indice_invalido_jogar_carta():
    """Testa jogada de carta com índice inválido."""
    jogador = Jogador("Player 1")
    
    resultado = jogador.jogar_carta(0)
    
    assert resultado is None
    assert jogador.carta_jogada is None
    print("✓ Índice inválido ao jogar carta")


if __name__ == "__main__":
    print("\n=== Executando testes de Jogador ===\n")
    
    test_criar_jogador_basico()
    test_receber_carta()
    test_jogar_carta()
    test_perder_vida()
    test_eliminacao_por_zero_vidas()
    test_criar_multiplos_jogadores()
    test_limpar_carta_jogada()
    test_get_info()
    test_indice_invalido_jogar_carta()
    
    print("\n=== Todos os testes passaram! ===\n")
