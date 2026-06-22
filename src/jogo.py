import pygame

from src.config import LARGURA_TELA, ALTURA_TELA, FPS, TITULO_JOGO
from src.baralho import criar_baralho, distribuir_cartas
from src.jogador import criar_jogadores
from src.entrada import tratar_eventos
from src.interface import (
    qual_carta_clicada,
    atualizar_display,
    desenhar_fim_de_jogo,
    desenhar_tela_inicial
)
from src.regras import (
    jogada_automatica,
    avaliar_vencedor_turno,
    verificar_fim_de_jogo,
    sortear_primeiro_dealer,
    passar_dealer,
    filtrar_ordem_ativos,
    avancar_turno,
    criar_ordem_esquerda, 
    criar_ordem_rodada
)
from src.dados import (
    salvar_resultado,
    obter_proximo_numero_partida
)

def executar_jogo():
    pygame.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
    relogio = pygame.time.Clock()

    baralho = criar_baralho()
    jogadores = criar_jogadores()

    ordem_mesa = [0, 2, 1, 3]

    indice_dealer = sortear_primeiro_dealer(len(jogadores))
    ordem_rodada = criar_ordem_rodada(indice_dealer, ordem_mesa)
    
    ordem_rodada_ativa = filtrar_ordem_ativos(ordem_rodada, jogadores)
    posicao_turno = 0
    indice_jogador_atual = ordem_rodada_ativa[posicao_turno]

    print(f"Primeiro a jogar: {jogadores[indice_jogador_atual].nome}")
    print(f"Dealer inicial: {jogadores[indice_dealer].nome}")
    print(f"Ordem da primeira rodada: {ordem_rodada}")

    momento_jogada = 0
    TEMPO_OPONENTES = 1000

    momento_jogada_jogador = 0
    TEMPO_JOGADOR = 20000

    momento_resultado = 0
    TEMPO_RESULTADO = 1500
    
    quantidade_distribuicao = 1
    baralho, jogadores = distribuir_cartas(baralho, jogadores, quantidade_distribuicao)

    jogador_principal = jogadores[0]
    oponentes = jogadores[1:]

    if indice_jogador_atual == 0:
        turno = "jogador"
        momento_jogada_jogador = pygame.time.get_ticks()
    else:
        turno = "oponente"
        momento_jogada = pygame.time.get_ticks()

    mesa = []
    donos_mesa = []
    rects_cartas_mao = []

    estado_partida = "inicio"
    mensagem_fim_de_jogo = ""
    mensagem_resultado = ""

    segundos_restantes = 20

    numero_partida = obter_proximo_numero_partida("data/resultado.txt")
    rodando = True

    while rodando:
        relogio.tick(FPS)
        rodando, pos_mouse = tratar_eventos()
        tempo_atual = pygame.time.get_ticks()

        if estado_partida == "inicio":
            desenhar_tela_inicial(tela)

            if pos_mouse is not None:
                estado_partida = "jogando"

                if indice_jogador_atual == 0:
                    momento_jogada_jogador = pygame.time.get_ticks()
                else:
                    momento_jogada = pygame.time.get_ticks()

            continue
        
        if (estado_partida == "jogando" and jogador_principal.esta_ativo() and turno == "jogador" and indice_jogador_atual == 0):
            indice_clicado = qual_carta_clicada(pos_mouse, rects_cartas_mao)
            segundos_restantes = (TEMPO_JOGADOR - (tempo_atual - momento_jogada_jogador)) // 1000

            if indice_clicado is not None:
                carta = jogador_principal.jogar_carta(indice_clicado)
                if carta:
                    mesa.append(carta)
                    donos_mesa.append(0)
                    posicao_turno, indice_jogador_atual, rodada_completa = avancar_turno(posicao_turno,ordem_rodada_ativa)

                    if rodada_completa:
                        turno = "avaliar"
                    else:
                        if indice_jogador_atual == 0:
                            turno = "jogador"
                            momento_jogada_jogador = pygame.time.get_ticks()
                        else:
                            turno = "oponente"
                            momento_jogada = pygame.time.get_ticks()

            elif tempo_atual - momento_jogada_jogador >= TEMPO_JOGADOR:
                carta = jogada_automatica(jogador_principal)
                if carta:
                    mesa.append(carta)
                    donos_mesa.append(0)
                    posicao_turno, indice_jogador_atual, rodada_completa = avancar_turno(posicao_turno,ordem_rodada_ativa)

                    if rodada_completa:
                        turno = "avaliar"
                    else:
                        if indice_jogador_atual == 0:
                            turno = "jogador"
                            momento_jogada_jogador = pygame.time.get_ticks()
                        else:
                            turno = "oponente"
                            momento_jogada = pygame.time.get_ticks()

                    print(f"[{jogador_principal.nome}] jogou automaticamente: {carta.valor} de {carta.naipe}")

        if (turno == "oponente" and estado_partida == "jogando" and tempo_atual - momento_jogada >= TEMPO_OPONENTES):
            jogador_atual = jogadores[indice_jogador_atual]
            carta_oponente = jogada_automatica(jogador_atual)

            if carta_oponente:
                mesa.append(carta_oponente)
                donos_mesa.append(indice_jogador_atual)

                print(
                    f"[{jogador_atual.nome}] jogou a carta: "
                    f"{carta_oponente.valor} de {carta_oponente.naipe}"
                )

                posicao_turno, indice_jogador_atual, rodada_completa = avancar_turno(
                    posicao_turno,
                    ordem_rodada_ativa
                )

                if rodada_completa:
                    turno = "avaliar"
                elif indice_jogador_atual == 0:
                    turno = "jogador"
                    momento_jogada_jogador = pygame.time.get_ticks()
                else:
                    turno = "oponente"
                    momento_jogada = pygame.time.get_ticks()

        if turno == "avaliar" and estado_partida == "jogando":
            vencedor_turno = avaliar_vencedor_turno(jogadores)

            if vencedor_turno is not None:
                print(f"Vencedor da rodada: {vencedor_turno.nome}")
                mensagem_resultado = (f"{vencedor_turno.nome} venceu a rodada!")

                indice_vencedor = jogadores.index(vencedor_turno)
                ordem_rodada = criar_ordem_esquerda(indice_vencedor,ordem_mesa)
                print(f"Ordem após o vencedor: {ordem_rodada}")

                for jogador in jogadores:
                    if jogador != vencedor_turno:
                        jogador.perder_vida(1)

                for jogador in jogadores:
                    print(f"{jogador.nome}: {jogador.vidas} vidas")

            else:
                print("Rodada anulada: não houve vencedor")
                mensagem_resultado = "Rodada anulada!"

            estado_partida = verificar_fim_de_jogo(jogador_principal, oponentes)

            if estado_partida == "derrota":
                print("Fim de jogo! Você perdeu.")
                mensagem_fim_de_jogo = "Fim de jogo! Você perdeu."

            elif estado_partida == "vitoria":
                print("Fim de jogo! Você venceu.")
                mensagem_fim_de_jogo = "Fim de jogo! Você venceu."

            if estado_partida != "jogando":
                salvar_resultado("data/resultado.txt", estado_partida, jogadores, numero_partida=numero_partida)

            turno = "resultado"
            momento_resultado = pygame.time.get_ticks()

        if (turno == "resultado" and tempo_atual - momento_resultado >= TEMPO_RESULTADO):
            for jogador in jogadores:
                jogador.limpar_carta_jogada()

            mesa.clear()
            donos_mesa.clear()
            mensagem_resultado = ""

            jogadores_ativos_sem_cartas = all(
                jogador.tamanho_mao() == 0
                for jogador in jogadores
                if jogador.esta_ativo()
            )

            if estado_partida == "jogando" and jogadores_ativos_sem_cartas:
                print("Distribuição encerrada!")

                quantidade_distribuicao += 1

                if quantidade_distribuicao > 5:
                    quantidade_distribuicao = 1

                indice_dealer = passar_dealer(
                    indice_dealer,
                    ordem_mesa
                )
                ordem_rodada = criar_ordem_rodada(
                    indice_dealer,
                    ordem_mesa
                )

                print(f"Novo dealer: {jogadores[indice_dealer].nome}")
                print(f"Nova ordem: {ordem_rodada}")

                baralho = criar_baralho()

                jogadores_ativos = [
                    jogador
                    for jogador in jogadores
                    if jogador.esta_ativo()
                ]

                baralho, jogadores_ativos = distribuir_cartas(
                    baralho,
                    jogadores_ativos,
                    quantidade_distribuicao
                )

                print(
                    f"Nova distribuição: "
                    f"{quantidade_distribuicao} cartas"
                )

            if estado_partida == "jogando":
                ordem_rodada_ativa = filtrar_ordem_ativos(ordem_rodada, jogadores)
                posicao_turno = 0
                indice_jogador_atual = ordem_rodada_ativa[posicao_turno]

                if indice_jogador_atual == 0:
                    turno = "jogador"
                    momento_jogada_jogador = pygame.time.get_ticks()
                else:
                    turno = "oponente"
                    momento_jogada = pygame.time.get_ticks()
            else:
                turno = "fim"
      
        rects_cartas_mao = atualizar_display(tela, jogadores, mesa, rects_cartas_mao, quantidade_distribuicao,turno, mensagem_resultado, segundos_restantes, donos_mesa, indice_dealer)

        if estado_partida != "jogando":
            desenhar_fim_de_jogo(tela, mensagem_fim_de_jogo, estado_partida, jogadores)
            pygame.display.flip()

if __name__ == "__main__":
    executar_jogo()