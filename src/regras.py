import random
from collections import Counter
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
    tela.fill(PRETO)


def desenhar_carta(tela, x, y, carta, mostrar_detalhes=True):
    rect = pygame.Rect(x, y, LARGURA_CARTA, ALTURA_CARTA)

    pygame.draw.rect(tela, COR_FUNDO_CARTA, rect)
    pygame.draw.rect(tela, COR_BORDA_CARTA, rect, ESPESSURA_BORDA_CARTA)

    if mostrar_detalhes and carta:
        fonte = pygame.font.Font(None, TAMANHO_FONTE_CARTA)

        # Trata o fato de que a carta pode ser um dicionário ou um objeto da classe Carta
        if isinstance(carta, dict):
            valor_texto = str(carta.get("valor", ""))
            naipe_original = carta.get("naipe", "")
        else:
            valor_texto = str(getattr(carta, "valor", ""))
            naipe_original = getattr(carta, "naipe", "")

        naipe_abrev = {
            "Paus": "♣",
            "Copas": "♥",
            "Espadas": "♠",
            "Ouros": "♦"
        }.get(naipe_original, "?")

        texto_principal = fonte.render(f"{valor_texto}{naipe_abrev}", True, COR_TEXTO_CARTA)
        texto_rect = texto_principal.get_rect(center=(x + LARGURA_CARTA // 2, y + ALTURA_CARTA // 2))
        tela.blit(texto_principal, texto_rect)

    return rect


def desenhar_mao_jogador(tela, jogador, rects_cartas):
    rects_cartas.clear()

    if not jogador or not hasattr(jogador, 'mao'):
        return rects_cartas

    cartas = jogador.mao
    total_cartas = len(cartas)

    if total_cartas == 0:
        return rects_cartas

    largura_total = total_cartas * LARGURA_CARTA + (total_cartas - 1) * ESPACAMENTO_CARTAS
    x_inicio = (LARGURA_TELA - largura_total) // 2
    y_inicio = ALTURA_TELA - MARGEM_INFERIOR

    for i, carta in enumerate(cartas):
        x = x_inicio + i * (LARGURA_CARTA + ESPACAMENTO_CARTAS)
        y = y_inicio
        rect = desenhar_carta(tela, x, y, carta, mostrar_detalhes=True)
        rects_cartas.append(rect)

    return rects_cartas


def desenhar_cartas_oponente_topo(tela, jogador, y_pos=MARGEM_SUPERIOR):
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
        rect = desenhar_carta(tela, x, y_pos, {"valor": "?", "naipe": ""}, mostrar_detalhes=False)
        rects_cartas.append(rect)

    return rects_cartas


def desenhar_cartas_oponente_esquerda(tela, jogador, x_pos=MARGEM_LATERAL):
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
    if not mesa:
        return

    x_centro = (LARGURA_TELA - LARGURA_CARTA) // 2
    y_centro = (ALTURA_TELA - ALTURA_CARTA) // 2

    cartas_visiveis = mesa[-3:] if len(mesa) > 3 else mesa

    for i, carta in enumerate(cartas_visiveis):
        x = x_centro + i * 20
        y = y_centro + i * 10
        desenhar_carta(tela, x, y, carta, mostrar_detalhes=True)


def atualizar_display(tela, jogadores, mesa, rects_cartas_mao):
    desenhar_tela(tela)

    if len(jogadores) >= 4:
        rects_cartas_mao = desenhar_mao_jogador(tela, jogadores[0], rects_cartas_mao)
        desenhar_cartas_oponente_topo(tela, jogadores[1])
        desenhar_cartas_oponente_esquerda(tela, jogadores[3])
        desenhar_cartas_oponente_direita(tela, jogadores[2])
        desenhar_mesa(tela, mesa)

    pygame.display.flip()
    return rects_cartas_mao


def qual_carta_clicada(pos_mouse, rects_cartas):
    if not pos_mouse:
        return None

    for i, retangulo in enumerate(rects_cartas):
        if retangulo.collidepoint(pos_mouse):
            return i

    return None


ORDEM_VALORES = {
    "7": 1,
    "6": 2,
    "5": 3,
    "4": 4,
    "3": 5,
    "2": 6,
    "A": 7,
}

ORDEM_NAIPES = {
    "Ouros": 1,
    "Espadas": 2,
    "Copas": 3,
    "Paus": 4,
}


def _obter_atributos_carta(carta):
    if carta is None:
        return None, None
    if isinstance(carta, dict):
        return carta.get("valor"), carta.get("naipe")
    return getattr(carta, "valor", None), getattr(carta, "naipe", None)


def obter_forca_carta(carta):
    """
    Retorna a força total da carta usando preferencialmente o método forca_total()
    da sua classe Carta para garantir compatibilidade com as novas regras.
    """
    if carta is None:
        return -1
        
    # Se for um objeto real da sua classe Carta, usa a lógica nativa dela
    if hasattr(carta, 'forca_total'):
        return carta.forca_total()

    # Fallback de segurança para dicionários (caso venham de mocks/testes do grupo)
    valor, naipe = _obter_atributos_carta(carta)
    if valor is None or naipe is None:
        return -1

    peso_valor = ORDEM_VALORES.get(str(valor), 0)
    peso_naipe = ORDEM_NAIPES.get(naipe, 0)
    return (peso_valor * 10) + peso_naipe


def comparar_cartas(carta1, carta2):
    if obter_forca_carta(carta1) >= obter_forca_carta(carta2):
        return carta1
    return carta2


def avaliar_vencedor_turno(jogadores):
    """
    Avalia o vencedor do turno respeitando a regra do TPC-16:
    - Cartas repetidas (valores iguais) se anulam e saem da disputa.
    - Exceção: Os Ases ('A') NÃO se anulam se forem repetidos. Eles permanecem válidos e disputam pelo naipe.
    """
    jogadores_com_jogada = [j for j in jogadores if getattr(j, "carta_jogada", None) is not None]

    if not jogadores_com_jogada:
        return None

    valores_na_mesa = [str(j.carta_jogada.valor) for j in jogadores_com_jogada]
    contagem_valores = Counter(valores_na_mesa)

    # Nova lista de jogadores válidos baseada na regra do TPC-16
    jogadores_validos = []
    for j in jogadores_com_jogada:
        val_str = str(j.carta_jogada.valor)
        
        # Se for um Ás ('A'), ele ignora a regra de anulação por repetição e vai pro jogo
        if val_str == "A":
            jogadores_validos.append(j)
        # Se for qualquer outro valor (2 a 7), só vale se for a única carta com esse valor na mesa
        elif contagem_valores[val_str] == 1:
            jogadores_validos.append(j)

    if not jogadores_validos:
        return None

    # Encontra o vencedor baseado na força total computada
    vencedor = max(jogadores_validos, key=lambda j: obter_forca_carta(j.carta_jogada))
    return vencedor


def verificar_derrota(jogador_principal):
    return jogador_principal.vidas <= 0


def verificar_vitoria(oponentes):
    return all(op.vidas <= 0 or op.esta_eliminado() for op in oponentes)


def verificar_fim_de_jogo(jogador_principal, oponentes):
    if verificar_derrota(jogador_principal):
        return "derrota"
    if verificar_vitoria(oponentes):
        return "vitoria"
    return "jogando"


def jogada_automatica(jogador):
    if jogador.esta_ativo() and len(jogador.mao) > 0:
        oponente_jogada = random.randint(0, (len(jogador.mao)-1))
        carta_jogada = jogador.jogar_carta(oponente_jogada)
        return carta_jogada
    if jogador.esta_ativo() and jogador.tamanho_mao() > 0:
        indice = random.randint(0, jogador.tamanho_mao() - 1)
        return jogador.jogar_carta(indice)
    return None


def sortear_primeiro_dealer(qtd_jogadores):
    """
    Sorteia aleatoriamente o índice do primeiro dealer.
    """
    return random.randint(0, qtd_jogadores - 1)


def passar_dealer(indice_atual, qtd_jogadores):
    """
    Passa o dealer para o próximo jogador à direita seguindo a ordem incremental (sentido horário).
    """
    return (indice_atual + 1) % qtd_jogadores