# Nome do Jogo

> Life of Cards

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.


## Integrantes do grupo

- Nome 1: Lorrainny Camille Aparecida 
- Nome 2: Matheus Oliveira Costa Torres
- Nome 3: Rafael Henrique da Pena Duarte
- Nome 4: Enzo Espíndola Sousa Broilo Rezende 

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte do jogo, incluindo cartas, jogadores, regras, interface e dados.
- `data/`: histórico dos resultados das partidas.
- `tests/`: testes de lógica, interface e integração.
- `docs/`: documentação do projeto, incluindo proposta inicial.

## Descrição do jogo

Life of Cards é um jogo de cartas para quatro jogadores, sendo um jogador controlado pelo usuário e três oponentes controlados pelo computador. 

Em cada rodada, o jogador escolhe uma carta usando o mouse. Os oponentes jogam automaticamente e as cartas são comparadas conforme a força da carta. As cartas seguem a ordem A, 2, 3, 4, 5, 6 e 7, da mais forte para a mais fraca.

Os jogadores que não vencerem a rodada perdem uma vida. A partida termina quando o jogador perde todas as suas vidas ou quando todos os oponentes são eliminados.

## Objetivo do jogador

O objetivo é preservar suas três vidas e eliminar os três oponentes antes de ser eliminado.

## Regras do jogo

- O jogo possui quatro jogadores: um jogador principal e três oponentes automáticos.
- Cada jogador começa com três vidas.
- Em cada rodada, o jogador principal escolhe uma carta e os oponentes jogam automaticamente.
- O vencedor da rodada mantém suas vidas. Todos os outros jogadores ativos perdem uma vida.
- Um jogador é eliminado quando suas vidas chegam a zero.
- O jogador vence ao eliminar todos os oponentes e perde ao ficar sem vidas.
- As distribuições seguem o ciclo de 1, 2, 3, 4 e 5 cartas. Depois, o ciclo volta para uma carta.
- O baralho possui 28 cartas. A ordem de força é: A > 2 > 3 > 4 > 5 > 6 > 7.
- Quando existem dois ou mais Ases, vence o naipe mais forte: Paus > Copas > Espadas > Ouros.
- Cartas repetidas de valores entre 2 e 7 anulam-se.
- Se todas as cartas válidas forem anuladas, a rodada termina sem vencedor e ninguém perde vida.

## Controles

- Botão esquerdo do mouse: selecionar e jogar uma carta.
- ESC: fechar o jogo.

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/lore-camisx/life-of-cards.git
cd life-of-cards
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m unittest discover -s tests -p "test_*.py" -v
python tests/test_interface.py
python tests/test_integracao.py
```

## Checklist mínimo para entrega

- Preencher este README com nome final, descrição real, regras e controles do jogo.
- Atualizar `docs/proposta.MD` com a proposta do grupo.
- Garantir que o jogo executa com `python main.py`.
- Garantir que os testes passam com `pytest`.

## Observações para os alunos

- Mantenham o código organizado em módulos pequenos e com responsabilidade clara.
- Comentem partes importantes da lógica, principalmente regras do jogo.
- Registrem decisões técnicas no README do grupo ao longo do desenvolvimento.
