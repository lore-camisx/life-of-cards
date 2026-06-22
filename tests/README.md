# Testes

Esta pasta contém os testes automatizados do projeto.

## Arquivos

- `test_baralho.py`: verifica a quantidade e a unicidade das cartas.
- `test_jogador.py`: verifica perda de vida e eliminação.
- `test_logica.py`: verifica força das cartas, regra dos Ases e condições de vitória e derrota.
- `test_interface.py`: verifica desenho das cartas, posicionamento e detecção de cliques.
- `test_integracao.py`: verifica distribuição, jogadas, vidas e renderização em conjunto.

## Como executar

Testes de lógica, jogador e baralho:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
python tests/test_interface.py
python tests/test_integracao.py
```