from src.config import VIDAS_MAXIMAS

class Jogador:
    """Representa um jogador no jogo Life of Cards."""

    VIDAS_INICIAIS = VIDAS_MAXIMAS

    def __init__(self, nome, id_jogador=None):
        """
        Inicializa um novo jogador.
        """
        self.nome = nome
        self.id = id_jogador
        self.vidas = self.VIDAS_INICIAIS
        self.mao = []
        self.carta_jogada = None
        self.ativo = True

    def receber_carta(self, carta):
        """
        Adiciona uma carta à mão do jogador.
        """
        if carta:
            self.mao.append(carta)

    def jogar_carta(self, indice):
        """
        Remove e retorna uma carta da mão do jogador.
        """
        if 0 <= indice < len(self.mao):
            self.carta_jogada = self.mao.pop(indice)
            return self.carta_jogada
        return None

    def perder_vida(self, quantidade=1):
        """
        Reduz as vidas do jogador.
        """
        self.vidas = max(0, self.vidas - quantidade)
        if self.vidas == 0:
            self.eliminar()

    def eliminar(self):
        """Marca o jogador como eliminado."""
        self.ativo = False

    def esta_eliminado(self):
        """
        Verifica se o jogador foi eliminado.
        """
        return self.vidas == 0 and not self.ativo

    def esta_ativo(self):
        """
        Verifica se o jogador ainda está ativo no jogo.
        """
        return self.ativo and self.vidas > 0

    def esta_vivo(self):
        """Alias para manter compatibilidade com regras e testes."""
        return self.esta_ativo()

    def tamanho_mao(self):
        """
        Retorna a quantidade de cartas na mão.
        """
        return len(self.mao)

    def limpar_carta_jogada(self):
        """Remove a referência da carta jogada."""
        self.carta_jogada = None

    def get_info(self):
        """
        Retorna informações do jogador em formato de dicionário.
        """
        return {
            "nome": self.nome,
            "id": self.id,
            "vidas": self.vidas,
            "mao_tamanho": len(self.mao),
            "ativo": self.ativo,
            "eliminado": self.esta_eliminado()
        }

    def __str__(self):
        """Representação em string do jogador."""
        status = "Ativo" if self.ativo else "Eliminado"
        return f"{self.nome} | Vidas: {self.vidas} | Cartas: {len(self.mao)} | Status: {status}"


def criar_jogador(nome, id_jogador=None):
    """Função auxiliar para criar um jogador."""
    return Jogador(nome, id_jogador)


def criar_jogadores():
    """
    Cria uma lista com os 4 jogadores iniciais.
    """
    jogadores = []
    nomes = ["Jogador 01", "Jogador 02", "Jogador 03", "Jogador 04"]

    for id_jogador, nome in enumerate(nomes, 1):
        jogador = Jogador(nome, id_jogador)
        jogadores.append(jogador)

    return jogadores