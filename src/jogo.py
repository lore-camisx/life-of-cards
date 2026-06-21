import pygame 
import sys
import os
import sys
import pygame

from src.config import LARGURA_TELA, ALTURA_TELA, FPS, TITULO_JOGO
from src.baralho import criar_baralho, distribuir_cartas
from src.jogador import criar_jogadores
from src.entrada import tratar_eventos
from src.interface import qual_carta_clicada, atualizar_display, renderizar_tudo
from src.regras import jogada_automatica, sortear_primeiro_dealer, passar_dealer
from src.dados import salvar_resultado 
from src.interface import qual_carta_clicada, atualizar_display
from src.interface import desenhar_fim_de_jogo
from src.regras import (
    jogada_automatica,
    avaliar_vencedor_turno,
    verificar_fim_de_jogo
)
from src.dados import salvar_resultado


def executar_jogo():
    pygame.init()

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

    jogador_principal = jogadores[0]
    oponentes = jogadores[1:]

    turno = "jogador"
    mesa = []
    rects_cartas_mao = []

    estado_partida = "jogando"
    mensagem_fim_de_jogo = ""

    rodando = True

    while rodando:
        relogio.tick(FPS)
        rodando, pos_mouse = tratar_eventos()
        
        if (estado_partida == "jogando" and jogador_principal.esta_ativo() and pos_mouse and turno == "jogador"):
            indice_clicado = qual_carta_clicada(pos_mouse, rects_cartas_mao)
            
            if indice_clicado is not None:
                carta = jogador_principal.jogar_carta(indice_clicado)
                
                if carta:
                    mesa.append(carta)
                    turno = "oponente"
                    print(f"[{jogador_principal.nome}] jogou a carta: {carta.valor} de {carta.naipe}")
        
        if turno == "oponente" and estado_partida == "jogando":
            
            for oponente in jogadores[1:]:
                carta_oponente = jogada_automatica(oponente)

                if carta_oponente:
                    mesa.append(carta_oponente)
                    turno = "jogador"
                    print(f"[{oponente.nome}] jogou a carta: {carta_oponente.valor} de {carta_oponente.naipe}")
            
            vencedor_turno = avaliar_vencedor_turno(jogadores)

            if vencedor_turno is not None:
                print(f"Vencedor da rodada: {vencedor_turno.nome}")

                for jogador in jogadores:
                    if jogador != vencedor_turno:
                        jogador.perder_vida(1)

                for jogador in jogadores:
                    print(f"{jogador.nome}: {jogador.vidas} vidas")

            else:
                print("Rodada anulada: não houve vencedor")

            estado_partida = verificar_fim_de_jogo(jogador_principal, oponentes)

            if estado_partida == "derrota":
                print("Fim de jogo! Você perdeu.")
                mensagem_fim_de_jogo = "Fim de jogo! Você perdeu."

            elif estado_partida == "vitoria":
                print("Fim de jogo! Você venceu.")
                mensagem_fim_de_jogo = "Fim de jogo! Você venceu."

            for jogador in jogadores:
                jogador.limpar_carta_jogada()

            mesa.clear()
            turno = "jogador"
                    
        tela.fill(COR_MESA)        
        rects_cartas_mao = atualizar_display(tela, jogadores, mesa, rects_cartas_mao)

        if estado_partida != "jogando":
            desenhar_fim_de_jogo(tela, mensagem_fim_de_jogo, estado_partida)

    pygame.display.flip()
    salvar_resultado("data/resultado.txt", "indefinido", jogadores, numero_partida=1)

import pygame
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from config import *
from interface import renderizar_tudo


def carregar_fontes():
    """Carrega as fontes usadas no jogo."""
    pygame.font.init()
    return {
        "grande":  pygame.font.SysFont("segoeui", FONTE_GRANDE, bold=True),
        "media":   pygame.font.SysFont("segoeui", FONTE_MEDIA,  bold=True),
        "pequena": pygame.font.SysFont("segoeui", FONTE_PEQUENA),
    }


def estado_inicial():
    """
    Retorna o estado inicial da partida:
    lista de jogadores + mensagem de status.
    """
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

        if estado_partida == "jogando":
            if pos_mouse and turno == "jogador" and jogador_principal.esta_ativo():
                indice_clicado = qual_carta_clicada(pos_mouse, rects_cartas_mao)

                if indice_clicado is not None:
                    carta = jogador_principal.jogar_carta(indice_clicado)
                    if carta:
                        mesa.append(carta)
                        turno = "oponente"

            if turno == "oponente":
                for oponente in oponentes:
                    if oponente.esta_ativo():
                        carta_oponente = jogada_automatica(oponente)
                        if carta_oponente:
                            mesa.append(carta_oponente)

                vencedor_turno = avaliar_vencedor_turno(jogadores)

                if vencedor_turno is not None:
                    for j in jogadores:
                        if j != vencedor_turno:
                            j.perder_vida(1)

                for j in jogadores:
                    j.limpar_carta_jogada()

                mesa.clear()
                turno = "jogador"

                estado_partida = verificar_fim_de_jogo(jogador_principal, oponentes)

                if estado_partida == "derrota":
                    mensagem_fim_de_jogo = "Fim de jogo! Você perdeu."
                    salvar_resultado("data/resultado.txt", "derrota", jogadores, numero_partida=1)

                elif estado_partida == "vitoria":
                    mensagem_fim_de_jogo = "Fim de jogo! Você venceu."
                    salvar_resultado("data/resultado.txt", "vitoria", jogadores, numero_partida=1)

        rects_cartas_mao = atualizar_display(tela, jogadores, mesa, rects_cartas_mao)

        if estado_partida != "jogando":
            fonte = pygame.font.SysFont("segoeui", 40, bold=True)
            cor_texto = (255, 50, 50) if estado_partida == "derrota" else (50, 255, 50)

            surf_msg = fonte.render(mensagem_fim_de_jogo, True, cor_texto)
            rect_msg = surf_msg.get_rect(center=(LARGURA_TELA // 2, ALTURA_TELA // 2))

            fundo_rect = pygame.Rect(
                rect_msg.x - 20,
                rect_msg.y - 10,
                rect_msg.width + 40,
                rect_msg.height + 20
            )

            pygame.draw.rect(tela, (0, 0, 0), fundo_rect, border_radius=8)
            pygame.draw.rect(tela, (255, 255, 255), fundo_rect, width=2, border_radius=8)
            tela.blit(surf_msg, rect_msg)
            pygame.display.flip()

        if not rodando:
            break

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    executar_jogo()