# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na Semana 1 do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com Python e Pygame dentro do prazo disponível.

## 1. Nome provisório do jogo

Nome provisório

Exemplo:

> Life of Cards 

## 2. Integrantes do grupo

Liste os integrantes do grupo.

- Nome 1: Lorrainny Camille Aparecida 
- Nome 2: Matheus Oliveira Costa Torres
- Nome 3: Rafael Henrique da Pena Duarte
- Nome 4: Enzo Espíndola Sousa Broilo Rezende *

## 3. Tipo de jogo

Indique o tipo de jogo que será desenvolvido.

Exemplos:

- jogo de desviar de obstáculos;
- jogo de coleta de itens;
- labirinto simples;
- jogo de perguntas e respostas;
- jogo de memória;
- Pong;
- Snake;
- Breakout;
- nave desviando de meteoros;
- corrida simples com obstáculos;
- jogo de clique rápido;
- jogo de sobrevivência simples.

Tipo escolhido pelo grupo:  

> Jogos de Cartas 

## 4. Descrição geral do jogo

Explique, em poucas linhas, como o jogo funcionará.

Procure responder:

- O que aparece na tela?
- O que o jogador controla?
- O que o jogador precisa fazer?
- Quais desafios aparecem durante a partida?

Descrição: 

> Na tela, uma mesa virtual animada distribui as cartas para os avatares dos usuários, destacando-se a rodada blind onde a carta fica visível na "testa" de todos, menos na do próprio dono. O jogador controla suas apostas iniciais e a escolha das cartas em cada turno, com o objetivo de prever exatamente suas vitórias para não perder vidas e acumular a menor pontuação final possível. Durante a partida, os maiores desafios enfrentados são a dedução lógica na rodada cega e a adaptação estratégica constante, já que as regras proíbem que a soma das apostas de todos os jogadores seja igual ao número de cartas daquela rodada.

## 5. Objetivo do jogador

Explique qual é o objetivo principal do jogador.

Exemplos:

- coletar o maior número possível de itens;
- sobreviver pelo maior tempo possível;
- chegar até o final do labirinto;
- acertar alvos;
- responder perguntas corretamente;
- evitar obstáculos;
- quebrar todos os blocos.

Objetivo:

> Preservar todas as vidas e acumular a menor pontuação final possível

## 6. Regras principais

Liste as principais regras do jogo.

Exemplo:

- O jogador começa com 3 vidas.
- Cada moeda coletada vale 10 pontos.
- Cada colisão com obstáculo remove 1 vida.
- A partida termina quando as vidas chegam a zero.
- O jogador vence se alcançar 100 pontos.

Regras do grupo:

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

## 7. Condição de vitória

Explique como o jogador vence ou conclui o jogo.

Exemplos:

- atingir determinada pontuação;
- chegar ao final da fase;
- sobreviver até o tempo acabar;
- responder uma quantidade mínima de perguntas;
- quebrar todos os blocos.

Condição de vitória:

> Sobreviver à partida fazendo com que todos os oponentes percam as suas 3 vidas primeiro.

## 8. Condição de derrota ou encerramento

Explique como o jogador perde ou quando a partida termina.

Exemplos:

- perder todas as vidas;
- acabar o tempo;
- colidir com determinado obstáculo;
- errar muitas perguntas;
- deixar a bola cair, no caso de Breakout ou Pong.

Condição de derrota ou encerramento:

> Perder as suas próprias 3 vidas durante os turnos.

## 9. Elementos previstos no jogo

Descreva os principais elementos que farão parte do jogo.

## Jogador ou elemento principal

Exemplo:

> Um personagem controlado pelas setas do teclado.

Descrição:

> ícone de jogador e as cartas controladas pelo mouse.

## Obstáculos, inimigos ou desafios

Exemplo:

> Obstáculos aparecem em posições aleatórias e devem ser evitados.

Descrição:

> Outros 3 jogadores na mesa e suas cartas.

## Itens, alvos ou objetos de interação

Exemplo:

> Moedas aparecem na tela e aumentam a pontuação quando coletadas.

Descrição:

> Cartas

## Pontuação, vidas, tempo ou progresso

Exemplo:

> O jogador começa com 3 vidas e ganha 10 pontos por item coletado.

Descrição:

> O jogador começa com 3 vidas e tem 20 segundos em cada turno para escolher sua carta.

## 10. Controles previstos

Informe os comandos que serão utilizados pelo jogador.

Exemplo:

- Seta para cima: mover para cima
- Seta para baixo: mover para baixo
- Seta para esquerda: mover para esquerda
- Seta para direita: mover para direita
- Espaço: realizar ação
- ESC: sair do jogo

Controles do grupo:

- Botão esquerdo do mouse: mover as cartas, selecionar as cartas, selecionar as opções de jogo

## 11. Organização inicial do código

Explique como o grupo pretende organizar o código.

Exemplo:

- `main.py`: inicia o jogo;
- `src/jogo.py`: contém o loop principal;
- `src/config.py`: guarda configurações como tamanho da tela e cores;
- `src/funcoes.py`: contém funções auxiliares;
- `src/dados.py`: contém funções de leitura e escrita de arquivos.

Organização planejada:

> 

- `main.py`: inicia o jogo;
- `src/config.py`: guarda configurações como tela, cores, FPS, vidas e tempo de turno;
- `src/jogo.py`: contém o loop principal da partida;
- `src/carta.py`: define as cartas, valores, naipes e forças;
- `src/baralho.py`: cria, embaralha e distribui as cartas;
- `src/jogador.py`: guarda informações dos jogadores, como vidas, mão e apostas;
- `src/regras.py`: controla as regras, comparação das cartas e vencedor do turno;
- `src/interface.py`: desenha mesa, cartas, jogadores, vidas e mensagens na tela;
- `src/entrada.py`: trata os cliques do mouse;
- `assets/`: guarda imagens, sons e fontes do jogo.


## 12. Recursos externos previstos

Informe se o grupo pretende utilizar imagens, sons, fontes, tutoriais ou códigos externos.

Exemplo:

- imagens obtidas de banco gratuito;
- sons gratuitos;
- tutorial usado apenas como referência;
- fonte personalizada.

Recursos previstos:

> assets de cartas, música de fundo (dóminio público), fonte personalizada, sons gratuitos, projetos e tutoriais usado apenas como referência, imagens gratuitas. 

Caso não pretenda utilizar recursos externos, escreva:

> Não pretendemos utilizar recursos externos.

## 13. Principais dificuldades esperadas

Liste as dificuldades que o grupo acredita que poderá enfrentar.

Exemplos:

- movimentação do jogador;
- colisão entre objetos;
- controle de tempo;
- criação do ranking;
- organização do código;
- uso do GitHub;
- testes;
- exibição de textos na tela.

Dificuldades previstas:

- Dificuldade 1: AI de jogador
- Dificuldade 2: Criação de multiplayer 
- Dificuldade 3: AI que controla o jogo 

## 14. Escopo mínimo para a entrega final

Descreva qual será a versão mínima aceitável do jogo.

Esta seção é importante para evitar que o grupo escolha uma ideia grande demais.

Exemplo:

> A versão mínima do jogo terá um personagem controlado pelo teclado, obstáculos aparecendo na tela, sistema de vidas, sistema de pontuação e tela de fim de jogo.

Escopo mínimo:

> A versão mínima do jogo terá um modo multiplayer de 4 jogadores, para realização do jogo de cartas. 

## 15. Possíveis melhorias, caso haja tempo

Liste funcionalidades extras que o grupo poderá implementar se conseguir concluir o escopo mínimo.

Exemplos:

- tela inicial;
- sons;
- fases;
- aumento de dificuldade;
- ranking;
- animações;
- novos tipos de obstáculos;
- diferentes personagens;
- menu de pausa.

Melhorias possíveis:

- Melhoria 1: Design mais sofisticado 
- Melhoria 2: Cartas com poderes especiais 
- Melhoria 3: Outros modos de jogo
- Melhoria 4: Maior eficiência da AI 