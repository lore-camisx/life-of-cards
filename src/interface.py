import pygame
from src.config import (
    PRETO, BRANCO, CINZA, CINZA_ESCURO,
    LARGURA_TELA, ALTURA_TELA,
    LARGURA_CARTA, ALTURA_CARTA, ESPACAMENTO_CARTAS,
    ESPESSURA_BORDA_CARTA, COR_BORDA_CARTA, COR_FUNDO_CARTA,
    COR_TEXTO_CARTA, TAMANHO_FONTE_CARTA,
    MARGEM_INFERIOR, MARGEM_SUPERIOR, MARGEM_LATERAL
)


def desenhar_tela(tela):
    """Limpa a tela e pinta de preto."""
    tela.fill(PRETO)


def desenhar_carta(tela, x, y, carta, mostrar_detalhes=True):
    """
    Desenha uma carta na tela.
    
    Args:
        tela: Superfície pygame
        x, y: Posição do canto superior esquerdo
        carta (dict): Carta com 'valor' e 'naipe'
        mostrar_detalhes (bool): Se True, mostra valor e naipe
        
    Returns:
        pygame.Rect: Retângulo da carta (para detecção de cliques)
    """
    rect = pygame.Rect(x, y, LARGURA_CARTA, ALTURA_CARTA)
    
    # Desenha fundo da carta
    pygame.draw.rect(tela, COR_FUNDO_CARTA, rect)
    pygame.draw.rect(tela, COR_BORDA_CARTA, rect, ESPESSURA_BORDA_CARTA)
    
    # Desenha valor e naipe se especificado
    if mostrar_detalhes and carta:
        fonte = pygame.font.Font(None, TAMANHO_FONTE_CARTA)
        
        valor_texto = str(carta.get("valor", "?"))
        naipe_abrev = {
            "Paus": "♣",
            "Copas": "♥",
            "Espadas": "♠",
            "Ouros": "♦"
        }.get(carta.get("naipe", ""), "?")
        
        # Texto principal (valor + naipe)
        texto_principal = fonte.render(f"{valor_texto}{naipe_abrev}", True, COR_TEXTO_CARTA)
        texto_rect = texto_principal.get_rect(center=(x + LARGURA_CARTA // 2, y + ALTURA_CARTA // 2))
        tela.blit(texto_principal, texto_rect)
    
    return rect


def desenhar_mao_jogador(tela, jogador, rects_cartas):
    """
    Desenha a mão do jogador principal na parte inferior da tela.
    
    Args:
        tela: Superfície pygame
        jogador: Objeto Jogador com atributo 'mao'
        rects_cartas (list): Lista para armazenar retângulos das cartas
        
    Returns:
        list: Lista atualizada com retângulos das cartas
    """
    rects_cartas.clear()
    
    if not jogador or not hasattr(jogador, 'mao'):
        return rects_cartas
    
    cartas = jogador.mao
    total_cartas = len(cartas)
    
    if total_cartas == 0:
        return rects_cartas
    
    # Calcula largura total
    largura_total = total_cartas * LARGURA_CARTA + (total_cartas - 1) * ESPACAMENTO_CARTAS
    
    # Posição inicial (centralizado horizontalmente)
    x_inicio = (LARGURA_TELA - largura_total) // 2
    y_inicio = ALTURA_TELA - MARGEM_INFERIOR
    
    # Desenha cada carta
    for i, carta in enumerate(cartas):
        x = x_inicio + i * (LARGURA_CARTA + ESPACAMENTO_CARTAS)
        y = y_inicio
        rect = desenhar_carta(tela, x, y, carta, mostrar_detalhes=True)
        rects_cartas.append(rect)
    
    return rects_cartas


def desenhar_cartas_oponente_topo(tela, jogador, y_pos=MARGEM_SUPERIOR):
    """
    Desenha cartas do oponente do topo (posicionadas horizontalmente).
    
    Args:
        tela: Superfície pygame
        jogador: Objeto Jogador com atributo 'mao'
        y_pos: Posição Y das cartas
        
    Returns:
        list: Lista de retângulos das cartas
    """
    rects_cartas = []
    
    if not jogador or not hasattr(jogador, 'mao'):
        return rects_cartas
    
    cartas = jogador.mao
    total_cartas = len(cartas)
    
    if total_cartas == 0:
        return rects_cartas
    
    largura_total = total_cartas * LARGURA_CARTA + (total_cartas - 1) * ESPACAMENTO_CARTAS
    x_inicio = (LARGURA_TELA - largura_total) // 2
    
    for i in range(total_cartas):
        x = x_inicio + i * (LARGURA_CARTA + ESPACAMENTO_CARTAS)
        # Desenha sem mostrar detalhes (cartas viradas/simplificadas)
        rect = desenhar_carta(tela, x, y_pos, {"valor": "?", "naipe": ""}, mostrar_detalhes=False)
        rects_cartas.append(rect)
    
    return rects_cartas


def desenhar_cartas_oponente_esquerda(tela, jogador, x_pos=MARGEM_LATERAL):
    """
    Desenha cartas do oponente à esquerda (posicionadas verticalmente).
    
    Args:
        tela: Superfície pygame
        jogador: Objeto Jogador com atributo 'mao'
        x_pos: Posição X das cartas
        
    Returns:
        list: Lista de retângulos das cartas
    """
    rects_cartas = []
    
    if not jogador or not hasattr(jogador, 'mao'):
        return rects_cartas
    
    cartas = jogador.mao
    total_cartas = len(cartas)
    
    if total_cartas == 0:
        return rects_cartas
    
    altura_total = total_cartas * ALTURA_CARTA + (total_cartas - 1) * ESPACAMENTO_CARTAS
    y_inicio = (ALTURA_TELA - altura_total) // 2
    
    for i in range(total_cartas):
        y = y_inicio + i * (ALTURA_CARTA + ESPACAMENTO_CARTAS)
        rect = desenhar_carta(tela, x_pos, y, {"valor": "?", "naipe": ""}, mostrar_detalhes=False)
        rects_cartas.append(rect)
    
    return rects_cartas


def desenhar_cartas_oponente_direita(tela, jogador, x_pos=None):
    """
    Desenha cartas do oponente à direita (posicionadas verticalmente).
    
    Args:
        tela: Superfície pygame
        jogador: Objeto Jogador com atributo 'mao'
        x_pos: Posição X das cartas (padrão: margem direita)
        
    Returns:
        list: Lista de retângulos das cartas
    """
    rects_cartas = []
    
    if x_pos is None:
        x_pos = LARGURA_TELA - MARGEM_LATERAL - LARGURA_CARTA
    
    if not jogador or not hasattr(jogador, 'mao'):
        return rects_cartas
    
    cartas = jogador.mao
    total_cartas = len(cartas)
    
    if total_cartas == 0:
        return rects_cartas
    
    altura_total = total_cartas * ALTURA_CARTA + (total_cartas - 1) * ESPACAMENTO_CARTAS
    y_inicio = (ALTURA_TELA - altura_total) // 2
    
    for i in range(total_cartas):
        y = y_inicio + i * (ALTURA_CARTA + ESPACAMENTO_CARTAS)
        rect = desenhar_carta(tela, x_pos, y, {"valor": "?", "naipe": ""}, mostrar_detalhes=False)
        rects_cartas.append(rect)
    
    return rects_cartas


def desenhar_mesa(tela, mesa):
    """
    Desenha as cartas jogadas no centro da mesa.
    
    Args:
        tela: Superfície pygame
        mesa (list): Lista de cartas na mesa
    """
    if not mesa:
        return
    
    # Posição central
    x_centro = (LARGURA_TELA - LARGURA_CARTA) // 2
    y_centro = (ALTURA_TELA - ALTURA_CARTA) // 2
    
    # Desenha no máximo as últimas 3 cartas sobrepostas
    cartas_visiaveis = mesa[-3:] if len(mesa) > 3 else mesa
    
    for i, carta in enumerate(cartas_visiaveis):
        x = x_centro + i * 20
        y = y_centro + i * 10
        desenhar_carta(tela, x, y, carta, mostrar_detalhes=True)


def atualizar_display(tela, jogadores, mesa, rects_cartas_mao):
    """
    Orquestra o desenho completo da tela com todos os elementos.
    
    Args:
        tela: Superfície pygame
        jogadores (list): Lista de 4 jogadores
        mesa (list): Cartas na mesa
        rects_cartas_mao (list): Lista para armazenar retângulos (jogador principal)
        
    Returns:
        list: Lista atualizada de retângulos das cartas do jogador
    """
    desenhar_tela(tela)
    
    if len(jogadores) >= 4:
        # Jogador principal (embaixo)
        rects_cartas_mao = desenhar_mao_jogador(tela, jogadores[0], rects_cartas_mao)
        
        # Oponente topo
        desenhar_cartas_oponente_topo(tela, jogadores[1])
        
        # Oponente esquerda
        desenhar_cartas_oponente_esquerda(tela, jogadores[3])
        
        # Oponente direita
        desenhar_cartas_oponente_direita(tela, jogadores[2])
        
        # Cartas da mesa
        desenhar_mesa(tela, mesa)
    
    pygame.display.flip()
    return rects_cartas_mao


def qual_carta_clicada(pos_mouse, rects_cartas):
    """Detecta qual carta foi clicada."""
    if not pos_mouse:
        return None
        
    for i, retangulo in enumerate(rects_cartas):
        if retangulo.collidepoint(pos_mouse):
            return i
            
    return None