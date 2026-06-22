import random
from collections import Counter

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
    return None


def sortear_primeiro_dealer(qtd_jogadores):
    """
    Sorteia aleatoriamente o índice do primeiro dealer.
    """
    return random.randint(0, qtd_jogadores - 1)


def passar_dealer(indice_atual, ordem_mesa):
    posicao_atual = ordem_mesa.index(indice_atual)
    proxima_posicao = (posicao_atual + 1) % len(ordem_mesa)

    return ordem_mesa[proxima_posicao]

def criar_ordem_rodada(indice_dealer, ordem_mesa):
    posicao_dealer = ordem_mesa.index(indice_dealer)

    depois_dealer = ordem_mesa[posicao_dealer + 1:]
    inicio_ate_dealer = ordem_mesa[:posicao_dealer + 1]

    return depois_dealer + inicio_ate_dealer

def filtrar_ordem_ativos(ordem_rodada, jogadores):
    ordem_ativa = []

    for indice in ordem_rodada:
        if jogadores[indice].esta_ativo():
            ordem_ativa.append(indice)

    return ordem_ativa

def avancar_turno(posicao_turno, ordem_ativa):
    nova_posicao = posicao_turno + 1

    if nova_posicao >= len(ordem_ativa):
        return nova_posicao, None, True

    indice_atual = ordem_ativa[nova_posicao]

    return nova_posicao, indice_atual, False

def criar_ordem_esquerda(indice_vencedor, ordem_mesa):
    posicao_vencedor = ordem_mesa.index(indice_vencedor)

    posicao_esquerda = (posicao_vencedor - 1) % len(ordem_mesa)

    return (
        ordem_mesa[posicao_esquerda:]
        + ordem_mesa[:posicao_esquerda]
    )