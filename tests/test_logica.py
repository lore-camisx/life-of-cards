import unittest
from src.jogador import Jogador
from src.regras import comparar_cartas, avaliar_vencedor_turno, verificar_derrota, verificar_vitoria


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

    def test_desempate_entre_ases(self):
        a_paus = CartaSimples("A", "Paus")
        a_copas = CartaSimples("A", "Copas")
        self.assertEqual(comparar_cartas(a_paus, a_copas), a_paus)

    def test_anulacao_cartas_iguais_na_mesa(self):
        j1 = Jogador("Jogador 1")
        j1.carta_jogada = CartaSimples("A", "Paus")

        j2 = Jogador("Jogador 2")
        j2.carta_jogada = CartaSimples("A", "Copas")

        j3 = Jogador("Jogador 3")
        j3.carta_jogada = CartaSimples("2", "Ouros")

        j4 = Jogador("Jogador 4")
        j4.carta_jogada = CartaSimples("5", "Espadas")

        vencedor = avaliar_vencedor_turno([j1, j2, j3, j4])
        self.assertEqual(vencedor, j3)

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


if __name__ == '__main__':
    unittest.main()