import unittest
from src.baralho import criar_baralho


class TestBaralho(unittest.TestCase):
    def test_quantidade_cartas_baralho(self):
        baralho = criar_baralho()
        self.assertEqual(len(baralho), 28)

    def test_nao_existem_cartas_repetidas(self):
        baralho = criar_baralho()
        combinacoes = {(carta.valor, carta.naipe) for carta in baralho}
        self.assertEqual(len(baralho), len(combinacoes))


if __name__ == '__main__':
    unittest.main()