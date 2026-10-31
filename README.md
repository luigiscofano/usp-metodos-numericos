<p align="center"><img src="assets/capa.svg" alt="Métodos Numéricos: um laboratório de experimentos reproduzíveis" width="100%"></p>

# Métodos Numéricos e Aplicações

[![Verificação numérica](https://github.com/luigiscofano/usp-metodos-numericos/actions/workflows/verificacao.yml/badge.svg?branch=main)](https://github.com/luigiscofano/usp-metodos-numericos/actions/workflows/verificacao.yml)

**Do algoritmo à evidência: notebooks, implementações didáticas, gráficos e testes para compreender aproximação, convergência e erro.**

Portfólio de **Luigi Scofano de Araujo · Engenharia de Computação, Poli-USP · USP 13680334**. Contexto: materiais de Métodos Numéricos e Aplicações de 2025. O nome da pasta recuperada identifica MAP312201/T01-Computação.

> **Procedência:** cinco notebooks foram recuperados e preservados em versões sanitizadas em `acervo/`. A pasta da disciplina lista ainda um sexto, de introdução a Python, cujo destino não foi recuperado. Os sete notebooks de `notebooks/` são roteiros novos/reelaborados nesta edição de 2026, com código verificável e identificação das extensões. Não são apresentados como cópias autenticadas de entregas acadêmicas. [Detalhes →](docs/PROCEDENCIA.md)

## Todos os notebooks de estudo

| Notebook | Conteúdo e experimento | Evidência de execução |
| --- | --- | --- |
| [01 · Python](notebooks/01_introducao_python.ipynb) | Arrays, funções, máscaras, vetorização e erros | Asserções, tabela e gráfico |
| [02 · Zeros e fractais](notebooks/02_zeros_fractais.ipynb) | Newton, raiz múltipla, ciclo e bacias complexas | Resíduos e pontos não convergidos explícitos |
| [03 · Ponto flutuante, Gauss e PLU](notebooks/03_ponto_flutuante_gauss.ipynb) | Cancelamento, pivotamento, precisão reduzida e Hilbert | PA=LU, solução conhecida e resíduo normalizado |
| [04 · DFT e FFT](notebooks/04_fft.ipynb) | Convenções, inversa, espectro, aliasing e custo | Comparação com NumPy e reconstrução do sinal |
| [05 · Interpolação](notebooks/05_interpolacao_newton.ipynb) | Newton, baricêntrica, Chebyshev, Runge e splines | Reprodução polinomial e curvas de erro |
| [06 · EDO e Chua](notebooks/06_edo_chua.ipynb) | Euler, Heun, RK4, estabilidade e pêndulo | Refinamento, energia e comparação com DOP853 |
| [07 · GPS sintético](notebooks/07_gps_sintetico.ipynb) | Gauss–Newton, pseudodistâncias e ECEF/geodésicas | Referência sintética, ruído e geometria degenerada |

**[Catálogo detalhado dos notebooks →](notebooks/README.md)** · **[Acervo recuperado →](acervo/README.md)** · **[Galeria de resultados →](assets/README.md)**

## Objetivos pedagógicos em destaque

A meta é **explicar quando uma aproximação é confiável e como demonstrar isso**:

- Distinguir erro, resíduo, tolerância e condicionamento.
- Implementar um método e confrontá-lo com solução analítica ou referência independente.
- Investigar convergência por refinamento e registrar motivos de falha.
- Entender custo computacional antes de aumentar o tamanho de um problema.
- Separar visualização atraente de evidência quantitativa.
- Produzir uma execução reproduzível em ambiente e kernel novos.

[OBJETIVOS_PEDAGOGICOS.md](docs/OBJETIVOS_PEDAGOGICOS.md) relaciona cada competência a uma atividade e a um critério de avaliação. Não há avaliação de eficácia pedagógica com participantes.

## Comece aqui

| Quero… | Ler/abrir |
| --- | --- |
| Executar os notebooks | [Instalação e reprodução](docs/INSTALACAO.md) |
| Saber o que veio da faculdade | [Procedência e inventário](docs/PROCEDENCIA.md) |
| Entender os métodos e hipóteses | [Guia matemático](docs/METODOS.md) |
| Conferir correções e complementos | [Decisões e diferenças](docs/CORRECOES.md) |
| Avaliar os testes e limites | [Validação](docs/VALIDACAO.md) |
| Navegar no código | [Biblioteca didática](numericos/README.md) |
| Apresentar o projeto | [Roteiro de apresentação](docs/APRESENTACAO.md) |

## Executar

Use Python 3.12 e um ambiente virtual. Na raiz:

```sh
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m ipykernel install --user --name python3 --display-name "Python 3"
python -m pytest -q
python scripts/executar_notebooks.py
```

O último comando executa cada notebook de estudo em kernel novo e exporta HTML, JSON de resultados e `.ipynb` executados para `build/`. **Não executa o acervo histórico**, que mantém problemas e lacunas identificados. Para ambientes sem servidor/kernel Jupyter disponível, há a alternativa documentada `python scripts/executar_sem_kernel.py`.

Não há downloads de dados, montagem de Drive, credenciais ou chamadas a serviços externos durante os experimentos. Os dados são analíticos ou sintéticos com seeds explícitas.

## Organização

| Diretório | Função |
| --- | --- |
| [notebooks/](notebooks/README.md) | Sete roteiros de estudo executáveis |
| [acervo/](acervo/README.md) | Cinco versões recuperadas e sanitizadas; 477 células originais |
| [numericos/](numericos/README.md) | Implementações reutilizáveis de seis famílias de métodos |
| [tests/](tests/README.md) | Testes com soluções conhecidas, referências e casos de falha |
| [docs/](docs/README.md) | Matemática, objetivos, procedência, validação e apresentação |
| [scripts/](scripts/README.md) | Validação do acervo e execução/exportação |
| [assets/](assets/README.md) | Figuras científicas produzidas pelos notebooks |

As dependências diretas do ambiente de reprodução estão fixadas em `requirements.txt`; o pacote didático e seus intervalos de compatibilidade estão em `pyproject.toml`. Isso não equivale a um lock completo de dependências transitivas.

## Validação confirmada

**29 testes aprovados em Linux, macOS e Windows; sete notebooks executados com kernel Jupyter novo.** [Execução confirmada](https://github.com/luigiscofano/usp-metodos-numericos/actions/runs/41222104656) · [Baixar HTMLs, notebooks executados e figuras](https://github.com/luigiscofano/usp-metodos-numericos/actions/runs/41222104656/artifacts/13050262644). O artefato da CI tem retenção de 90 dias e pode exigir login no GitHub; os fontes permanecem neste repositório.

## Histórico de organização

As entregas estão divididas por biblioteca numérica, notebooks, acervo, testes/automação e documentação. As branches e os [PRs integrados](docs/PUBLICACAO.md) registram mudanças reais desta edição, sem datas retroativas ou revisões fictícias. [Guia de contribuição](CONTRIBUTING.md).

**Limites principais:** implementações para estudo, aritmética finita, FFT radix-2, DFT densa com limite de memória, EDO de passo fixo e GPS simplificado. Não são substitutos gerais para bibliotecas científicas de produção nem para validação física.
