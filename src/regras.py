import random

def jogada_automatica(jogador):
    """O oponente joga uma carta aleatória da mão se estiver ativo."""
    if jogador.esta_ativo() and len(jogador.mao) > 0:
        oponente_jogada = random.randint(0, (len(jogador.mao)-1))
        carta_jogada = jogador.jogar_carta(oponente_jogada)
        return carta_jogada
    return None

# --- LÓGICA DO DEALER (TPC-14) ---
def sortear_primeiro_dealer(total_jogadores):
    """Sorteia o índice do primeiro dealer de forma aleatória."""
    return random.randint(0, total_jogadores - 1)

def passar_dealer(indice_dealer_atual, total_jogadores):
    """Garante que a rotação do dealer siga sempre a ordem para a direita."""
    return (indice_dealer_atual + 1) % total_jogadores