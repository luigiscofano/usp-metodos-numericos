# Métodos Numéricos · Sete experimentos reproduzíveis

> Notebooks e biblioteca Python para estudar raízes, sistemas lineares, FFT, interpolação, EDO e GPS sintético, com gráficos, asserções e acervo acadêmico separado.

![Visão geral de Métodos Numéricos · Sete experimentos reproduzíveis](assets/capa.svg)

[![Verificação](https://github.com/luigiscofano/usp-metodos-numericos/actions/workflows/verificacao.yml/badge.svg?branch=main)](https://github.com/luigiscofano/usp-metodos-numericos/actions/workflows/verificacao.yml)

[O que faz](#o-que-este-projeto-faz) · [Módulos](#funcionalidades-e-módulos) · [Executar](#como-executar) · [Aprendizagem](#o-que-desenvolvi-e-aprendi) · [Estado atual](#estado-atual) · [Documentação](#documentação-e-navegação)

## O que este projeto faz

É um laboratório de computação científica com **sete notebooks de estudo**. Cada roteiro explica um problema, implementa ou utiliza métodos numéricos e compara resultados por gráficos, resíduos e testes. Uma biblioteca Python reúne implementações reutilizáveis; cinco notebooks recuperados da disciplina ficam preservados em `acervo/`.

Um notebook mistura texto, fórmulas, código e resultados. Ele pode ser lido no GitHub, aberto em um editor Jupyter ou executado automaticamente para gerar HTML. Os roteiros de estudo são independentes; não é preciso executar os sete para usar apenas um método da biblioteca.

## Qual problema resolve

Computadores representam números com precisão finita e frequentemente resolvem problemas por aproximação. O projeto ajuda a distinguir uma resposta que apenas parece plausível de uma aproximação sustentada por critérios de erro, convergência e referência. Também torna explícitos casos de falha: derivada pequena, sistema mal condicionado, passo instável ou geometria inadequada.

## Funcionalidades e módulos

### Catálogo dos sete roteiros

| Roteiro | Problema e mecanismos | O que observar |
| --- | --- | --- |
| [01 · Python](notebooks/01_introducao_python.ipynb) | Arrays, funções, máscaras, vetorização e tratamento de erros | Asserções, tabelas e gráfico; introdução ao ambiente |
| [02 · Zeros e fractais](notebooks/02_zeros_fractais.ipynb) | Newton real/complexo, raízes múltiplas, ciclos e bacias de atração | Resíduo, motivo de parada e pontos sem convergência |
| [03 · Ponto flutuante e PLU](notebooks/03_ponto_flutuante_gauss.ipynb) | Cancelamento, Gauss, pivotamento, precisão reduzida e Hilbert | PA=LU, solução conhecida e resíduo relativo |
| [04 · DFT e FFT](notebooks/04_fft.ipynb) | Transformada discreta, inversa, espectro, aliasing e custo | Reconstrução do sinal e comparação com NumPy |
| [05 · Interpolação](notebooks/05_interpolacao_newton.ipynb) | Diferenças divididas, forma baricêntrica, Chebyshev, Runge e splines | Reprodução polinomial e curvas de erro |
| [06 · EDO e Chua](notebooks/06_edo_chua.ipynb) | Euler, Heun, RK4, estabilidade, pêndulo e circuito de Chua | Refinamento de passo, energia e comparação com DOP853 |
| [07 · GPS sintético](notebooks/07_gps_sintetico.ipynb) | Pseudodistâncias, Gauss–Newton, ECEF e coordenadas geodésicas | Efeito de ruído e de geometria degenerada |

### Biblioteca didática

[numericos/](numericos/README.md) contém seis famílias: `raizes`, `lineares`, `fourier`, `interpolacao`, `edo` e `gps`. Podem ser importadas a partir da raiz ou instaladas em modo editável. São implementações para entender o mecanismo, com validação de entradas e limites explícitos; não substituem de modo geral bibliotecas científicas de produção.

### Acervo recuperado

Os cinco arquivos em [acervo/](acervo/README.md) preservam os conteúdos recuperados, incluindo lacunas e limitações, com 477 células originais. Os créditos do material docente foram mantidos. Essa pasta **não é executada pelo exportador dos sete roteiros**. A introdução a Python da edição histórica não foi recuperada; o primeiro roteiro é uma substituição nova. O GPS é uma extensão desta edição.

## Como executar

```sh
git clone https://github.com/luigiscofano/usp-metodos-numericos.git
cd usp-metodos-numericos
```

Crie um ambiente com **Python 3.12**:

```sh
python -m venv .venv
```

Ative-o no terminal que você usa:

| Sistema | Comando |
| --- | --- |
| Windows / PowerShell | `.\.venv\Scripts\Activate.ps1` |
| Linux / macOS | `source .venv/bin/activate` |

Se seu sistema oferece apenas `python3`, use esse nome ao criar o ambiente. A partir daqui, execute os comandos na raiz do repositório, com o ambiente ativado.

```sh
python -m pip install -r requirements.txt
```

Registre o kernel usado pelo executor dos notebooks:

```sh
python -m ipykernel install --user --name python3 --display-name "Python 3"
```


### Testar, validar o acervo e executar os roteiros

```sh
python -m pytest -q
python scripts/verificar_acervo.py
python scripts/executar_notebooks.py
```

O último comando inicia um kernel novo para cada notebook e deve informar `PASS` para os sete roteiros. Os arquivos executados, versões HTML e `resultados-notebooks.json` ficam em `build/`; figuras SVG ficam em `assets/figuras/`. Abra os HTMLs no navegador para ler os resultados sem instalar uma interface Jupyter.

Para uso interativo, abra um `.ipynb` em um editor compatível e selecione o Python do ambiente preparado. JupyterLab pode ser instalado à parte; ele não é necessário para a exportação acima.

### Usar um método diretamente

```sh
python -c "from numericos.raizes import newton; print(newton(lambda x: x*x-2, lambda x: 2*x, 1.0))"
```

A aproximação deve ficar próxima de √2; examine também o critério de término e os campos retornados. Não use apenas um gráfico como prova de convergência.

### Ambiente sem kernel disponível

`python scripts/executar_sem_kernel.py` executa as células com IPython em um processo novo por roteiro. É uma alternativa documentada, mas não valida o protocolo Jupyter. O executor padrão e a CI fazem essa verificação separadamente.

### Problemas frequentes

| Sintoma | O que conferir |
| --- | --- |
| Kernel `python3` ausente | Registro do kernel no ambiente utilizado |
| Importação de `numericos` falha | Diretório corrente e ambiente; opcionalmente `python -m pip install -e .` |
| FFT rejeita tamanho 3 | Esta implementação radix-2 exige potência de dois |
| DFT rejeita entrada grande | Limite intencional de memória da matriz densa |
| EDO ou Newton não convergem | Passo, derivada, condição inicial e motivo de parada; não suprima o erro para aprovar o resultado |

## O que desenvolvi e aprendi

A edição de estudo reúne biblioteca, roteiros reelaborados, experimentos, figuras, testes e exportação. A [procedência](docs/PROCEDENCIA.md) identifica o que foi recuperado e o que foi implementado nesta edição, sem atribuir os materiais docentes exclusivamente ao aluno.

**Objetivos pedagógicos:** distinguir erro e resíduo; explicar condicionamento; investigar convergência por refinamento; comparar um método com referência independente; estimar custo antes de aumentar o problema; repetir a execução em ambiente e kernel novos. O [guia pedagógico](docs/OBJETIVOS_PEDAGOGICOS.md) relaciona essas competências a atividades verificáveis.

## Estado atual

| Disponível | Limite / evolução |
| --- | --- |
| Sete roteiros, biblioteca e figuras | Edição de estudo, distinta dos arquivos históricos |
| 29 testes e execução automatizada dos notebooks | Dependências diretas fixadas, sem lock completo de transitivas |
| Dados analíticos/sintéticos, seeds explícitas | Sem dados GNSS reais ou validação física do GPS |
| Métodos e falhas documentados | FFT radix-2, DFT densa limitada, EDO de passo fixo e GPS simplificado |

## Validação e limites

A CI inclui testes em Linux, macOS e Windows e execução com kernel Jupyter. Consulte [VALIDACAO.md](docs/VALIDACAO.md) e o badge para a evidência da versão testada. Os experimentos não precisam de credenciais, montagem de Drive ou download de dados. Os artefatos de CI têm retenção limitada; os fontes e figuras permanecem versionados.

## Documentação e navegação

[Catálogo dos notebooks](notebooks/README.md) · [Biblioteca](numericos/README.md) · [Acervo](acervo/README.md) · [Testes](tests/README.md) · [Scripts](scripts/README.md) · [Figuras](assets/README.md) · [Documentação](docs/README.md) · [Guia matemático](docs/METODOS.md) · [Correções](docs/CORRECOES.md) · [Apresentação](docs/APRESENTACAO.md) · [PRs](docs/PUBLICACAO.md)


## Autoria, referências e licença

**Luigi Scofano de Araujo · Engenharia de Computação, Poli-USP · USP 13680334.** Fontes recuperados, componentes de terceiros e trabalhos em grupo mantêm os créditos indicados nos arquivos e na documentação.

[Procedência](docs/PROCEDENCIA.md) · [Como contribuir](CONTRIBUTING.md) · [Mudanças](CHANGELOG.md)

## Tópicos do repositório

`python` · `jupyter-notebook` · `numerical-methods` · `scientific-computing` · `linear-algebra` · `fft` · `interpolation` · `differential-equations` · `gps` · `numpy` · `usp`
