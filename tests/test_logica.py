import unittest
from src.jogador import Jogador
from src.regras import (
    comparar_cartas,
    passar_dealer,
    avaliar_vencedor_turno,
    verificar_derrota,
    verificar_vitoria,
    filtrar_ordem_ativos,
    avancar_turno,
    criar_ordem_rodada
)


class CartaSimples:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe


class TestRegras(unittest.TestCase):
    def test_comparacao_forca_cartas(self):
        a_ouros = CartaSimples("A", "Ouros")
        dois_paus = CartaSimples("2", "Paus")
        dois_copas = CartaSimples("2", "Copas")
        tres_espadas = CartaSimples("3", "Espadas")

        self.assertEqual(comparar_cartas(a_ouros, dois_paus), a_ouros)
        self.assertEqual(comparar_cartas(dois_copas, tres_espadas), dois_copas)

    def test_ases_repetidos_desempatam_pelo_naipe(self):
        a_paus = CartaSimples("A", "Paus")
        a_copas = CartaSimples("A", "Copas")
        self.assertEqual(comparar_cartas(a_paus, a_copas), a_paus)

    def test_ases_iguais_na_mesa_desempatam_pelo_naipe(self):
        j1 = Jogador("Jogador 1")
        j1.carta_jogada = CartaSimples("A", "Paus")

        j2 = Jogador("Jogador 2")
        j2.carta_jogada = CartaSimples("A", "Copas")

        j3 = Jogador("Jogador 3")
        j3.carta_jogada = CartaSimples("2", "Ouros")

        j4 = Jogador("Jogador 4")
        j4.carta_jogada = CartaSimples("5", "Espadas")

        vencedor = avaliar_vencedor_turno([j1, j2, j3, j4])
        self.assertEqual(vencedor, j1)

    def test_vitoria_e_derrota(self):
        principal = Jogador("Principal")
        oponente1 = Jogador("Oponente 1")
        oponente2 = Jogador("Oponente 2")
        oponente3 = Jogador("Oponente 3")

        principal.vidas = 0
        principal.eliminar()
        self.assertTrue(verificar_derrota(principal))

        principal.vidas = 3
        principal.ativo = True
        oponente1.vidas = 0
        oponente1.eliminar()
        oponente2.vidas = 0
        oponente2.eliminar()
        oponente3.vidas = 0
        oponente3.eliminar()

        self.assertTrue(verificar_vitoria([oponente1, oponente2, oponente3]))

    def test_criar_ordem_rodada(self):
        ordem_mesa = [0, 2, 1, 3]

        resultado = criar_ordem_rodada(0, ordem_mesa)

        self.assertEqual(criar_ordem_rodada(0, ordem_mesa), [2, 1, 3, 0])
        self.assertEqual(criar_ordem_rodada(2, ordem_mesa), [1, 3, 0, 2])
        self.assertEqual(criar_ordem_rodada(1, ordem_mesa), [3, 0, 2, 1])
        self.assertEqual(criar_ordem_rodada(3, ordem_mesa), [0, 2, 1, 3])

        self.assertEqual(passar_dealer(0, ordem_mesa), 2)
        self.assertEqual(passar_dealer(2, ordem_mesa), 1)
        self.assertEqual(passar_dealer(1, ordem_mesa), 3)
        self.assertEqual(passar_dealer(3, ordem_mesa), 0)

    def test_filtrar_ordem_ativos(self):
        jogadores = [
            Jogador("Jogador 0"),
            Jogador("Jogador 1"),
            Jogador("Jogador 2"),
            Jogador("Jogador 3")
        ]

        jogadores[1].eliminar()

        ordem = [2, 1, 3, 0]
        resultado = filtrar_ordem_ativos(ordem, jogadores)

        self.assertEqual(resultado, [2, 3, 0])

    def test_sequencia_de_turnos(self):
        ordem_ativa = [2, 1, 3, 0]
        posicao_turno = 0
        jogadores_que_jogaram = []

        while posicao_turno < len(ordem_ativa):
            indice_atual = ordem_ativa[posicao_turno]
            jogadores_que_jogaram.append(indice_atual)
            posicao_turno += 1

        self.assertEqual(jogadores_que_jogaram, [2, 1, 3, 0])
        self.assertEqual(posicao_turno, 4)

    def test_avancar_turno(self):
        ordem = [2, 1, 3, 0]

        resultado = avancar_turno(0, ordem)
        self.assertEqual(resultado, (1, 1, False))

        resultado = avancar_turno(3, ordem)
        self.assertEqual(resultado, (4, None, True))

if __name__ == '__main__':
    unittest.main()