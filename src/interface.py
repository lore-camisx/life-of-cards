import pygame
from src.config import *

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
    if jogador.esta_eliminado():
        return f"{jogador.nome} — ELIMINADO"

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
        fonte_nome = pygame.font.SysFont("segoeuisymbol", 20)
        informacoes = criar_texto_jogador(jogador)
        texto_nome = fonte_nome.render(
            informacoes,
            True,
            COR_TEXTO_NOME
        )

        texto_rect = texto_nome.get_rect(
            center=(LARGURA_TELA // 2, ALTURA_TELA - 130)
        )

        tela.blit(texto_nome, texto_rect)
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
        fonte_nome = pygame.font.SysFont("segoeuisymbol", 20)
        informacoes = criar_texto_jogador(jogador)
        texto_nome = fonte_nome.render(informacoes, True, COR_TEXTO_NOME)

        texto_rect = texto_nome.get_rect(
            center=(LARGURA_TELA // 2, 120)
        )

        tela.blit(texto_nome, texto_rect)
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
        fonte_nome = pygame.font.SysFont("segoeuisymbol", 20)
        informacoes = criar_texto_jogador(jogador)
        texto_nome = fonte_nome.render(informacoes, True, COR_TEXTO_NOME)

        texto_rect = texto_nome.get_rect(
            midleft=(x_pos + LARGURA_CARTA + 10, ALTURA_TELA // 2)
        )

        tela.blit(texto_nome, texto_rect)
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
        fonte_nome = pygame.font.SysFont("segoeuisymbol", 20)
        informacoes = criar_texto_jogador(jogador)
        texto_nome = fonte_nome.render(informacoes, True, COR_TEXTO_NOME)

        texto_rect = texto_nome.get_rect(
            midright=(x_pos - 10, ALTURA_TELA // 2)
        )

        tela.blit(texto_nome, texto_rect)
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


def desenhar_mesa(tela, mesa, donos_mesa=None):
    """
    Desenha as cartas jogadas no centro da mesa.
    
    Args:
        tela: Superfície pygame
        mesa (list): Lista de cartas na mesa
    """
    if not mesa:
        return
    
    centro_x = LARGURA_TELA // 2
    centro_y = ALTURA_TELA // 2

    posicoes = [
    # jogador principal — abaixo
        (centro_x - LARGURA_CARTA // 2, centro_y + 60),

    # oponente superior — acima
        (centro_x - LARGURA_CARTA // 2, centro_y - ALTURA_CARTA - 60),

    # oponente direito
        (centro_x + 100, centro_y - ALTURA_CARTA // 2),

    # oponente esquerdo
        (centro_x - LARGURA_CARTA - 100, centro_y - ALTURA_CARTA // 2),
    ]
    
    for i, carta in enumerate(mesa):
        indice_posicao = i

        if donos_mesa is not None:
            indice_posicao = donos_mesa[i]

        if indice_posicao < len(posicoes):
            x, y = posicoes[indice_posicao]
            desenhar_carta(tela, x, y, carta, mostrar_detalhes=True)

def desenhar_distribuicao(tela, quantidade):
    """Mostra a quantidade de cartas da distribuição atual."""

    fonte = pygame.font.SysFont("segoeui", 20, bold=True)

    palavra = "carta" if quantidade == 1 else "cartas"
    mensagem = f"Distribuição: {quantidade} {palavra}"

    texto = fonte.render(
        mensagem,
        True,
        COR_TEXTO_NOME
    )

    fundo = texto.get_rect(topleft=(20, 20))
    fundo = fundo.inflate(20, 12)

    pygame.draw.rect(
        tela,
        (20, 55, 25),
        fundo,
        border_radius=6
    )

    pygame.draw.rect(
        tela,
        COR_BORDA_CARTA,
        fundo,
        width=2,
        border_radius=6
    )

    tela.blit(texto, texto.get_rect(center=fundo.center))

def desenhar_indicador_turno(tela, turno, mensagem_resultado=""):
    """Mostra quem deve jogar."""

    fonte = pygame.font.SysFont("segoeui", 22, bold=True)

    if turno == "jogador":
        mensagem = "SUA VEZ"
        cor = (255, 220, 80)

    elif turno == "oponente":
        mensagem = "OPONENTES JOGANDO"
        cor = (210, 210, 220)

    else:
        mensagem = mensagem_resultado
        cor = (100, 220, 130)

    texto = fonte.render(mensagem, True, cor)

    texto_rect = texto.get_rect(
        center=(LARGURA_TELA // 2, ALTURA_TELA // 2 - 80)
    )

    fundo_rect = texto_rect.inflate(30, 16)

    pygame.draw.rect(
        tela,
        (15, 45, 20),
        fundo_rect,
        border_radius=7
    )

    pygame.draw.rect(
        tela,
        cor,
        fundo_rect,
        width=2,
        border_radius=7
    )

    tela.blit(texto, texto_rect)

def desenhar_dealer(tela, indice_dealer):
    fonte = pygame.font.SysFont("segoeui", 18, bold=True)
    texto = fonte.render("DEALER", True, (255, 215, 0))

    posicoes = [
        (LARGURA_TELA // 2, ALTURA_TELA - 125),  # jogador 0
        (LARGURA_TELA // 2, 145),                # jogador 1
        (LARGURA_TELA - 160, ALTURA_TELA // 2),  # jogador 2
        (160, ALTURA_TELA // 2)                  # jogador 3
    ]

    x, y = posicoes[indice_dealer]
    tela.blit(texto, texto.get_rect(center=(x, y)))

def atualizar_display(tela, jogadores, mesa, rects_cartas_mao, quantidade_distribuicao=None,turno=None, mensagem_resultado="", segundos_restantes=None, donos_mesa=None, indice_dealer=None):
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
        desenhar_mesa(tela, mesa, donos_mesa)

    if quantidade_distribuicao is not None:
        desenhar_distribuicao(tela, quantidade_distribuicao)

    if turno is not None:
        desenhar_indicador_turno(tela, turno, mensagem_resultado)

    if segundos_restantes is not None and turno == "jogador":
        fonte_timer = pygame.font.SysFont("segoeuisymbol", 28, bold=True)
        cor_timer = (255, 80, 80) if segundos_restantes <= 5 else (255, 220, 80)
        texto_timer = fonte_timer.render(f"⏱ {segundos_restantes}s", True, cor_timer)
        tela.blit(texto_timer, texto_timer.get_rect(center=(LARGURA_TELA // 2, ALTURA_TELA - 160)))
    
    if indice_dealer is not None:
        desenhar_dealer(tela, indice_dealer)
    
    pygame.display.flip()
    return rects_cartas_mao

def desenhar_fim_de_jogo(tela, mensagem, estado_partida, jogadores):
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

    fonte_info = pygame.font.SysFont("segoeui", 24)

    y = texto_rect.bottom + 30

    for jogador in jogadores:
        texto_jogador = fonte_info.render(
        f"{jogador.nome}: {jogador.vidas} vidas",
        True,
        (255, 255, 255)
    )

        tela.blit(
            texto_jogador,
            texto_jogador.get_rect(center=(LARGURA_TELA // 2, y))
        )

        y += 35

    texto_saida = fonte_info.render(
    "ESC - Sair",
    
    True,
    (255, 255, 0)
    )

    tela.blit(
    texto_saida,
    texto_saida.get_rect(center=(LARGURA_TELA // 2, y + 30))
    )

def qual_carta_clicada(pos_mouse, rects_cartas):
    """Detecta qual carta foi clicada."""
    if not pos_mouse:
        return None
        
    for i, retangulo in enumerate(rects_cartas):
        if retangulo.collidepoint(pos_mouse):
            return i
        
def desenhar_tela_inicial(tela):
    fonte_titulo = pygame.font.SysFont("segoeui", 50, bold=True)
    fonte_texto = pygame.font.SysFont("segoeui", 26)

    tela.fill(COR_TELA)

    titulo = fonte_titulo.render(
        "Life of Cards",
        True,
        BRANCO
    )

    instrucao = fonte_texto.render(
        "Clique para iniciar",
        True,
        (255, 220, 80)
    )

    objetivo = fonte_texto.render(
        "Objetivo:",
        True,
        BRANCO
    )

    descricao = fonte_texto.render(
        "Sobreviva e elimine os oponentes antes de perder suas vidas.",
        True,
        BRANCO
    )

    tela.blit(
        titulo,
        titulo.get_rect(center=(LARGURA_TELA//2, 180))
    )

    tela.blit(
        instrucao,
        instrucao.get_rect(center=(LARGURA_TELA//2, 300))
    )

    tela.blit(
        objetivo,
        objetivo.get_rect(center=(LARGURA_TELA//2, 400))
    )

    tela.blit(
        descricao,
        descricao.get_rect(center=(LARGURA_TELA//2, 450))
    )

    pygame.display.flip()
            
    return None

