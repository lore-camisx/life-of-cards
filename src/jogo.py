import pygame 

from src.config import LARGURA_TELA, ALTURA_TELA, FPS, TITULO_JOGO, PRETO
from src.baralho import criar_baralho, distribuir_cartas
from src.jogador import criar_jogadores
from src.entrada import tratar_eventos
from src.interface import qual_carta_clicada, atualizar_display

def executar_jogo(): 
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
    relogio = pygame.time.Clock()

    baralho = criar_baralho()
    jogadores = criar_jogadores()
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
                    print(f"[{jogador_atual.nome}] jogou a carta: {carta['valor']} de {carta['naipe']}")

        rects_cartas_mao = atualizar_display(tela, jogadores, mesa, rects_cartas_mao)