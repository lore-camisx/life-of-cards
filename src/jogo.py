import sys
import pygame

from src.config import LARGURA_TELA, ALTURA_TELA, FPS, TITULO_JOGO
from src.baralho import criar_baralho, distribuir_cartas
from src.jogador import criar_jogadores
from src.entrada import tratar_eventos
from src.interface import qual_carta_clicada, atualizar_display
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