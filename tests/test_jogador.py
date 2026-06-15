import unittest
from src.jogador import Jogador


class TestJogador(unittest.TestCase):
    def test_perda_de_vida_comum(self):
        jogador = Jogador("Teste")
        jogador.vidas = 3
        jogador.perder_vida(1)
        self.assertEqual(jogador.vidas, 2)
        self.assertTrue(jogador.esta_ativo())

    def test_eliminacao_ao_zerar_vidas(self):
        jogador = Jogador("Teste")
        jogador.vidas = 1
        jogador.perder_vida(1)
        self.assertEqual(jogador.vidas, 0)
        self.assertTrue(jogador.esta_eliminado())
        self.assertFalse(jogador.esta_ativo())


if __name__ == '__main__':
    unittest.main()