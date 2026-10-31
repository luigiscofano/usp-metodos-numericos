# Catálogo dos notebooks de estudo

Todos os roteiros deste diretório foram preparados/reelaborados nesta edição, em 2026. Os conteúdos recuperados de 2025 estão preservados separadamente em [acervo/](../acervo/README.md). Os dois conjuntos não devem ser confundidos.

| Ordem | Notebook | Pré-requisito | Pergunta central |
| --- | --- | --- | --- |
| 1 | [Python](01_introducao_python.ipynb) | Aritmética e funções | Como representar e testar uma aproximação? |
| 2 | [Zeros e fractais](02_zeros_fractais.ipynb) | Derivadas e complexos | Como Newton converge e como falha? |
| 3 | [Ponto flutuante e Gauss](03_ponto_flutuante_gauss.ipynb) | Matrizes e sistemas | Resíduo pequeno significa solução precisa? |
| 4 | [DFT e FFT](04_fft.ipynb) | Exponenciais complexas | Como amostragem e convenção mudam o espectro? |
| 5 | [Interpolação](05_interpolacao_newton.ipynb) | Polinômios e funções | Por que aumentar o grau pode piorar a aproximação? |
| 6 | [EDO e Chua](06_edo_chua.ipynb) | Derivadas e sistemas | O comportamento observado é físico ou numérico? |
| 7 | [GPS sintético](07_gps_sintetico.ipynb) | Sistemas e mínimos quadrados | Como posição, relógio e geometria interagem? |

## Execução e saídas

Abra na raiz ou dentro de `notebooks/`, execute as células na ordem e use um kernel novo. As figuras são salvas em `assets/figuras/`. A galeria no fim de cada notebook referencia essas figuras; resultados textuais e contadores da execução local são preservados.

O exportador de kernel Jupyter gera versões completas executadas e HTML em `build/`. O executor local sem kernel usa IPython em processo separado para cada arquivo; esse modo é identificado na metadata e não é apresentado como uma sessão de kernel Jupyter.

## Classificação de procedência

- **01:** substituição nova para o tema introdutório cujo arquivo histórico ainda não foi recuperado.
- **02–06:** reelaborações de estudo dos temas presentes nos cinco notebooks recuperados. Não copiam integralmente todas as questões originais nem alegam que as respostas históricas estavam completas.
- **07:** extensão nova com dados sintéticos; não houve recuperação de um notebook histórico de GPS.

O acervo e os roteiros somam 12 notebooks disponíveis nesta edição. Há ainda um título histórico identificado, com recuperação pendente.
