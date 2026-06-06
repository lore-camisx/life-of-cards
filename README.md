# Nome do Jogo

> Life of Cards

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.


## Integrantes do grupo

- Nome 1: Lorrainny Camille Aparecida 
- Nome 2: Matheus Oliveira Costa Torres
- Nome 3: Rafael Henrique da Pena Duarte
- Nome 4: Enzo Espíndola Sousa Broilo Rezende *

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte principal do jogo (loop, regras, sprites e dados).
- `assets/`: imagens, fontes e sons.
- `data/`: arquivos persistentes (recorde/ranking).
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo proposta inicial.

## Descrição do jogo

> Na tela, uma mesa virtual animada distribui as cartas para os avatares dos usuários, destacando-se a rodada blind onde a carta fica visível na "testa" de todos, menos na do próprio dono. O jogador controla suas apostas iniciais e a escolha das cartas em cada turno, com o objetivo de prever exatamente suas vitórias para não perder vidas e acumular a menor pontuação final possível. Durante a partida, os maiores desafios enfrentados são a dedução lógica na rodada cega e a adaptação estratégica constante, já que as regras proíbem que a soma das apostas de todos os jogadores seja igual ao número de cartas daquela rodada.

## Objetivo do jogador

> Preservar todas as vidas e acumular a menor pontuação final possível

## Regras do jogo

- Regra 1: O jogo comporta exatamente 4 jogadores, cada um iniciando com 3 vidas.
- Regra 2: A partida termina imediatamente quando o jogador perde as suas 3 vidas, ou quando todos os seus oponentes perdem as 3 vidas.
- Regra 3: Cada jogador terá um limite de tempo de 20 segundos para escolher a sua carta. Se o tempo esgotar, uma carta aleatória da mão será jogada automaticamente.
- Regra 4: O jogo flui num ciclo contínuo de 5 distribuições de cartas: 1 carta por jogador na 1ª distribuição, 2 na 2ª, até 5 cartas na 5ª. Após isso, o ciclo recomeça.
- Regra 5: O Dealer (quem distribui) da 1ª distribuição é escolhido aleatoriamente pelo sistema. Nas distribuições seguintes, o papel de Dealer passa para o jogador à direita do Dealer anterior.
- Regra 6: A primeira pessoa a jogar a carta na mesa é sempre o jogador à direita do Dealer atual. Nos turnos subsequentes (dentro da mesma distribuição), o primeiro a jogar será sempre o jogador à esquerda de quem venceu o turno anterior.
- Regra 7: O baralho possui 28 cartas, sendo a ordem de força absoluta: A (Mais forte) > 2 > 3 > 4 > 5 > 6 > 7 (Mais fraca).
- Regra 8: Em caso de disputa entre Ases (Manilhas), a força é decidida pelos naipes: Paus > Copas > Espadas > Ouros.
- Regra 9: Se duas ou mais cartas de valor igual forem jogadas na mesa, elas anulam-se mutuamente e são descartadas. O vencedor do turno será o jogador que colocou a próxima carta de maior valor que não foi anulada.
- Regra 10: Em caso de empate total no valor das cartas, a turno é anulado.

## Controles

- Botão esquerdo do mouse: mover as cartas, selecionar as cartas, selecionar as opções de jogo

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone LINK_DO_REPOSITORIO
cd NOME_DA_PASTA
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
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
