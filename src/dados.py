def salvar_recorde(caminho_arquivo, pontuacao):
    """Salva a pontuação recorde em arquivo texto."""
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(str(pontuacao))


def carregar_recorde(caminho_arquivo):
    """Carrega o recorde salvo; retorna 0 se não existir valor válido."""
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()

            if conteudo == "":
                return 0

            return int(conteudo)

    except FileNotFoundError:
        return 0
    
def salvar_resultado(caminho_arquivo, resultado, jogadores, numero_partida):

    with open(caminho_arquivo, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"Partida {numero_partida} \nResultado: {resultado}")
        for jogador in jogadores:
            arquivo.write(f"\n{jogador}")

def carregar_historico(caminho_arquivo):
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            historico = arquivo.read().strip()

            if historico == "":
                return str("")

            return str(historico)

    except FileNotFoundError:
        return str("")