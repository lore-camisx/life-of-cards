import pygame 
import sys
import os

from src.config import *
from src.baralho import criar_baralho, distribuir_cartas
from src.jogador import criar_jogadores
from src.entrada import tratar_eventos
from src.interface import qual_carta_clicada, atualizar_display, renderizar_tudo
from src.regras import jogada_automatica, sortear_primeiro_dealer, passar_dealer
from src.dados import salvar_resultado 

def executar_jogo(): 
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
    relogio = pygame.time.Clock()

    baralho = criar_baralho()
    jogadores = criar_jogadores()
    
    # ==========================================
    # --- TESTE DO DEALER ROTATIVO (TPC-14) ---
    # ==========================================
    indice_dealer = sortear_primeiro_dealer(len(jogadores))
    
    print("\n--- TESTE DO DEALER ROTATIVO ---")
    for distribuicao in range(1, 6):
        nome_do_dealer = jogadores[indice_dealer].nome
        print(f"Distribuição {distribuicao}: Dealer = {nome_do_dealer}")
        
        # Passa o dealer para o próximo jogador
        indice_dealer = passar_dealer(indice_dealer, len(jogadores))
    print("--------------------------------\n")
    # ==========================================

    baralho, jogadores = distribuir_cartas(baralho, jogadores, 5)
    
    jogador_atual = jogadores[0]
    turno = "jogador"
    mesa = []
    rects_cartas_mao = [] 

    rodando = True
 
    while rodando:
        relogio.tick(FPS)
        rodando, pos_mouse = tratar_eventos()

        if pos_mouse and turno == "jogador":
            indice_clicado = qual_carta_clicada(pos_mouse, rects_cartas_mao)
            
            if indice_clicado is not None:
                carta = jogador_atual.jogar_carta(indice_clicado)
                if carta:
                    mesa.append(carta)
                    turno = "oponente"
                    print(f"[{jogador_atual.nome}] jogou a carta: {carta.valor} de {carta.naipe}")
        
        if turno == "oponente":
            for oponente in jogadores[1:]:
                carta_oponente = jogada_automatica(oponente)
                if carta_oponente:
                    mesa.append(carta_oponente)
                    print(f"[{oponente.nome}] jogou a carta: {carta_oponente.valor} de {carta_oponente.naipe}")
            
            # Atualiza a mesa, dá um delayzinho pra ver as cartas e limpa
            rects_cartas_mao = atualizar_display(tela, jogadores, mesa, rects_cartas_mao)
            pygame.time.delay(1000)
            mesa.clear()
            turno = "jogador"
                
        if turno != "oponente":
            rects_cartas_mao = atualizar_display(tela, jogadores, mesa, rects_cartas_mao)

    salvar_resultado("data/resultado.txt", "indefinido", jogadores, numero_partida=1)


# --- CÓDIGO DA SUA EQUIPE (NÃO MEXER) ---
sys.path.insert(0, os.path.dirname(__file__))

def carregar_fontes():
    pygame.font.init()
    return {
        "grande":  pygame.font.SysFont("segoeui", FONTE_GRANDE, bold=True),
        "media":   pygame.font.SysFont("segoeui", FONTE_MEDIA,  bold=True),
        "pequena": pygame.font.SysFont("segoeui", FONTE_PEQUENA),
    }

def estado_inicial():
    jogadores = [
        {"nome": JOGADOR_NOMES[0], "vidas": JOGADOR_VIDAS[0],
         "posicao": "baixo",    "principal": True},
        {"nome": JOGADOR_NOMES[1], "vidas": JOGADOR_VIDAS[1],
         "posicao": "esquerda", "principal": False},
        {"nome": JOGADOR_NOMES[2], "vidas": JOGADOR_VIDAS[2],
         "posicao": "cima",     "principal": False},
        {"nome": JOGADOR_NOMES[3], "vidas": JOGADOR_VIDAS[3],
         "posicao": "direita",  "principal": False},
    ]
    mensagem = "Aguardando início da partida..."
    return jogadores, mensagem

def main():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
    relogio = pygame.time.Clock()

    fontes = carregar_fontes()
    jogadores, mensagem_status = estado_inicial()

    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False

        renderizar_tudo(tela, fontes, jogadores, mensagem_status)
        pygame.display.flip()

        relogio.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()