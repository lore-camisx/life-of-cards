import pygame
from src.config import (
    LARGURA_TELA, ALTURA_TELA, COR_TELA,
    LARGURA_CARTA, ALTURA_CARTA, ESPACAMENTO_CARTAS,
    ESPESSURA_BORDA_CARTA, COR_BORDA_CARTA, COR_FUNDO_CARTA,
    COR_TEXTO_CARTA, TAMANHO_FONTE_CARTA,
    MARGEM_INFERIOR, MARGEM_SUPERIOR, MARGEM_LATERAL
)


def desenhar_tela(tela):
    """Limpa a tela e pinta de preto."""
    tela.fill(COR_TELA)


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

    '''Desenha as cartas'''
    sombra = pygame.Rect(
        x + 3,
        y + 3,
        LARGURA_CARTA,
        ALTURA_CARTA
    )

    pygame.draw.rect(
    tela,
    (20, 35, 20),
    sombra,
    border_radius=7
    )

    pygame.draw.rect(
        tela,
        COR_FUNDO_CARTA,
        rect,
        border_radius=7
    )

    pygame.draw.rect(
        tela,
        COR_BORDA_CARTA,
        rect,
        ESPESSURA_BORDA_CARTA,
        border_radius=7
    )
    
    # Desenha valor e naipe se especificado
    if not mostrar_detalhes and carta:
        cor_verso = (35, 45, 75)

        pygame.draw.rect(
            tela,
            cor_verso,
            rect,
            border_radius=7
        )

        borda_interna = rect.inflate(-8, -8)

        pygame.draw.rect(
            tela,
            (190, 150, 70),
            borda_interna,
            width=2,
            border_radius=5
        )

        pygame.draw.line(
        tela,
        (80, 95, 135),
        borda_interna.topleft,
        borda_interna.bottomright,
        2
        )

    else:
        fonte = pygame.font.SysFont("segoeuisymbol",TAMANHO_FONTE_CARTA)
        fonte_canto = pygame.font.SysFont("segoeuisymbol",12)
        
        valor_texto = str(carta.valor)
        naipe_abrev = {
            "Paus": "♣",
            "Copas": "♥",
            "Espadas": "♠",
            "Ouros": "♦"
        }.get(carta.naipe, "?")

        if carta.naipe in ["Copas", "Ouros"]:
            cor_naipe = (190, 35, 45)
        else:
            cor_naipe = (25, 25, 30)
        
        # Texto principal (valor + naipe)
        texto_principal = fonte.render(f"{valor_texto}{naipe_abrev}",True,cor_naipe)
        texto_canto = fonte_canto.render(f"{valor_texto}{naipe_abrev}",True,cor_naipe)
        tela.blit(texto_canto, (x + 6, y + 5))
        texto_rect = texto_principal.get_rect(center=(x + LARGURA_CARTA // 2, y + ALTURA_CARTA // 2))
        tela.blit(texto_principal, texto_rect)
    
    return rect

def criar_texto_jogador(jogador):
    """Monta o texto visual com as informações do jogador."""

    coracoes = "♥" * jogador.vidas
    quantidade = len(jogador.mao)

    return f"{jogador.nome}  {coracoes}  Cartas: {quantidade}"

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

    fonte_nome = pygame.font.SysFont("segoeuisymbol", 20)
    informacoes = criar_texto_jogador(jogador)
    texto_nome = fonte_nome.render(informacoes,True,COR_TEXTO_NOME)
    texto_rect = texto_nome.get_rect(centerx=x_inicio + largura_total // 2,bottom=y_inicio - 8)
    tela.blit(texto_nome, texto_rect)
    
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

    fonte_nome = pygame.font.SysFont("segoeuisymbol", 20)
    informacoes = criar_texto_jogador(jogador)
    texto_nome = fonte_nome.render(informacoes,True,COR_TEXTO_NOME)
    tela.blit(texto_nome, texto_nome.get_rect(centerx=x_inicio + largura_total // 2, y=y_pos + ALTURA_CARTA + 5))
    
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

    fonte_nome = pygame.font.SysFont("segoeuisymbol", 20)
    informacoes = criar_texto_jogador(jogador)
    texto_nome = fonte_nome.render(informacoes,True,COR_TEXTO_NOME)
    tela.blit(texto_nome, (x_pos + LARGURA_CARTA + 5, y_inicio + altura_total // 2))
    
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

    fonte_nome = pygame.font.SysFont("segoeuisymbol", 20)
    informacoes = criar_texto_jogador(jogador)
    texto_nome = fonte_nome.render(informacoes,True,COR_TEXTO_NOME)
    tela.blit(texto_nome, (x_pos - texto_nome.get_width() - 5, y_inicio + altura_total // 2))
    
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

def desenhar_fim_de_jogo(tela, mensagem, estado_partida):
    """Desenha a mensagem final de vitória ou derrota."""

    fonte = pygame.font.SysFont("segoeui", 40, bold=True)

    if estado_partida == "vitoria":
        cor_texto = (80, 220, 100)
    else:
        cor_texto = (230, 70, 70)

    texto = fonte.render(
        mensagem,
        True,
        cor_texto
    )

    texto_rect = texto.get_rect(
        center=(LARGURA_TELA // 2, ALTURA_TELA // 2)
    )

    fundo_rect = texto_rect.inflate(50, 30)

    pygame.draw.rect(
    tela,
    (8, 28, 21),
    fundo_rect,
    border_radius=10
    )

    pygame.draw.rect(
        tela,
        BRANCO,
        fundo_rect,
        width=2,
        border_radius=10
    )
    
    tela.blit(texto, texto_rect)


def qual_carta_clicada(pos_mouse, rects_cartas):
    """Detecta qual carta foi clicada."""
    if not pos_mouse:
        return None
        
    for i, retangulo in enumerate(rects_cartas):
        if retangulo.collidepoint(pos_mouse):
            return i
            
    return None

import pygame
from src.config import *


def desenhar_fundo_mesa(tela):
    """Pinta o fundo da tela com a cor da mesa (feltro verde)."""
    tela.fill(COR_MESA)


def desenhar_area_central(tela, fonte_media, fonte_pequena):
    """Área central onde as cartas jogadas serão exibidas."""
    rect = pygame.Rect(AREA_CENTRAL_X, AREA_CENTRAL_Y, AREA_CENTRAL_W, AREA_CENTRAL_H)

    sombra = pygame.Rect(rect.x + 4, rect.y + 4, rect.width, rect.height)
    pygame.draw.rect(tela, (15, 45, 15), sombra, border_radius=8)

    pygame.draw.rect(tela, COR_AREA_CARTA, rect, border_radius=8)

    pygame.draw.rect(tela, COR_BORDA, rect, width=2, border_radius=8)
    pygame.draw.rect(tela, (255, 255, 200), rect.inflate(-6, -6), width=1, border_radius=6)

    label = fonte_media.render("Cartas Jogadas", True, COR_TEXTO)
    tela.blit(label, (rect.centerx - label.get_width() // 2, rect.y + 10))

    slot_w, slot_h = 55, 80
    total = 4
    gap = 10
    total_w = total * slot_w + (total - 1) * gap
    start_x = rect.centerx - total_w // 2
    slot_y = rect.y + 45

    for i in range(total):
        sx = start_x + i * (slot_w + gap)
        slot_rect = pygame.Rect(sx, slot_y, slot_w, slot_h)
        pygame.draw.rect(tela, (15, 50, 15), slot_rect, border_radius=5)
        pygame.draw.rect(tela, (80, 120, 80), slot_rect, width=1, border_radius=5)

        cx, cy = slot_rect.centerx, slot_rect.centery
        pygame.draw.line(tela, (40, 80, 40), (cx - 8, cy), (cx + 8, cy), 1)
        pygame.draw.line(tela, (40, 80, 40), (cx, cy - 8), (cx, cy + 8), 1)


def _slot_rect_jogador(posicao):
    """
    Retorna o pygame.Rect do slot de cada jogador.
    posicao: 'baixo' | 'esquerda' | 'cima' | 'direita'
    """
    cx, cy = LARGURA // 2, ALTURA // 2

    if posicao == "baixo": 
        return pygame.Rect(cx - SLOT_W // 2, ALTURA - SLOT_H - 20, SLOT_W, SLOT_H)
    elif posicao == "esquerda":
        return pygame.Rect(20, cy - SLOT_H // 2, SLOT_W, SLOT_H)
    elif posicao == "cima": 
        return pygame.Rect(cx - SLOT_W // 2, 20, SLOT_W, SLOT_H)
    elif posicao == "direita": 
        return pygame.Rect(LARGURA - SLOT_W - 20, cy - SLOT_H // 2, SLOT_W, SLOT_H)


def desenhar_slot_jogador(tela, fontes, nome, vidas, posicao, eh_principal=False):
    """
    Desenha o slot (área) de um jogador na posição indicada.
    fontes: dict com 'grande', 'media', 'pequena'
    """
    cor_fundo = COR_JOGADOR if eh_principal else COR_OPONENTE
    rect = _slot_rect_jogador(posicao)

    sombra = pygame.Rect(rect.x + 3, rect.y + 3, rect.width, rect.height)
    pygame.draw.rect(tela, (0, 0, 0, 80), sombra, border_radius=8)

    pygame.draw.rect(tela, cor_fundo, rect, border_radius=8)

    espessura_borda = 3 if eh_principal else 1
    pygame.draw.rect(tela, COR_BORDA, rect, width=espessura_borda, border_radius=8)

    surf_nome = fontes["media"].render(nome, True, COR_TEXTO_NOME)
    tela.blit(surf_nome, (rect.x + 10, rect.y + 10))

    _desenhar_vidas(tela, fontes["pequena"], vidas, rect)

    if eh_principal:
        badge = fontes["pequena"].render("▶ VOCÊ", True, (255, 220, 50))
        tela.blit(badge, (rect.right - badge.get_width() - 8, rect.y + 8))


def _desenhar_vidas(tela, fonte, vidas, slot_rect):
    """Desenha corações representando as vidas dentro do slot."""

    label = fonte.render("Vidas:", True, COR_TEXTO)
    tela.blit(label, (slot_rect.x + 10, slot_rect.y + 40))

    # Corações preenchidos = vidas restantes, vazios = perdidas
    max_vidas = 5
    coracoes_x = slot_rect.x + 60
    coracoes_y = slot_rect.y + 40

    for i in range(max_vidas):
        if i < vidas:
            cor = COR_VIDA
            simbolo = "♥"
        else:
            cor = (80, 60, 60)
            simbolo = "♡"

        surf = fonte.render(simbolo, True, cor)
        tela.blit(surf, (coracoes_x + i * 22, coracoes_y))

    contagem = fonte.render(f"{vidas}/{max_vidas}", True, (200, 200, 200))
    tela.blit(contagem, (slot_rect.x + 10, slot_rect.y + 62))


def desenhar_todos_jogadores(tela, fontes, jogadores):
    """
    Desenha os 4 slots de jogadores.
    jogadores: lista de dicts com 'nome', 'vidas', 'posicao', 'principal'
    """
    for j in jogadores:
        desenhar_slot_jogador(
            tela, fontes,
            nome=j["nome"],
            vidas=j["vidas"],
            posicao=j["posicao"],
            eh_principal=j.get("principal", False),
        )


def desenhar_mensagem_status(tela, fonte, mensagem):
    """Exibe a mensagem de status da partida no centro-inferior da tela."""
    padding_x, padding_y = 20, 8
    surf = fonte.render(mensagem, True, COR_TEXTO)
    bg_w = surf.get_width() + padding_x * 2
    bg_h = surf.get_height() + padding_y * 2

    bg_x = LARGURA // 2 - bg_w // 2
    bg_y = ALTURA - SLOT_H - 20 - bg_h - 10

    bg_rect = pygame.Rect(bg_x, bg_y, bg_w, bg_h)
    pygame.draw.rect(tela, (0, 0, 0), bg_rect, border_radius=6)
    pygame.draw.rect(tela, COR_STATUS, bg_rect, width=1, border_radius=6)

    tela.blit(surf, (bg_x + padding_x, bg_y + padding_y))


def desenhar_titulo(tela, fonte):
    """Nome do jogo no topo centralizado."""
    surf = fonte.render("♠  LIFE OF CARDS  ♣", True, COR_TEXTO_NOME)
    tela.blit(surf, (LARGURA // 2 - surf.get_width() // 2, 2))


def renderizar_tudo(tela, fontes, jogadores, mensagem_status):
    """
    Função principal de renderização — chamada a cada frame pelo loop em jogo.py.
    Ordem: mesa → área central → jogadores → status → título
    """
    desenhar_mesa(tela)
    desenhar_area_central(tela, fontes["media"], fontes["pequena"])
    desenhar_todos_jogadores(tela, fontes, jogadores)
    desenhar_mensagem_status(tela, fontes["pequena"], mensagem_status)
    desenhar_titulo(tela, fontes["media"])
