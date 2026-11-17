# Fractais: estudo complementar

[README principal](../README.md) · [Notebook executado](../notebooks/08_fractais_exploracao.ipynb)

## Escopo

Roteiro novo de 2026, separado do acervo acadêmico histórico. Complementa o roteiro 02 sem substituir seus testes de convergência. Imagens calculadas numericamente, sem fotografias ou ilustrações geradas como substituto do cálculo.

| Família | Construção | Parâmetros padrão |
| --- | --- | --- |
| Mandelbrot | z ← z² + c; z inicial zero | 80 iterações, raio 4, janela [-2,3; 0,9] × [-1,067; 1,067] |
| Julia | z ← z² + c; condição inicial por pixel | c = −0,8 + 0,156i; 80 iterações, raio 4 |
| Burning Ship | z ← (abs(Re z) + i abs(Im z))² + c | detalhe [-1,82; −1,70] × [-0,09; −0,01] |
| Barnsley | quatro transformações afins probabilísticas | 30 mil pontos, semente 42, descarte inicial de 100 |
| Newton | raízes de z³ − 1 | até 30 passos, resíduo < 1e-10, derivada mínima 1e-14 |

## Executar e exportar

Abra o notebook em Jupyter ou no Google Colab e execute em ordem. É independente da biblioteca local `numericos`, para permitir abertura isolada. Usa apenas NumPy e Matplotlib; para reproduzir o ambiente exato, consulte `requirements.txt` na raiz. A versão didática usa malha 600 × 400, 80 iterações de escape, 30 passos de Newton e 30 mil pontos de Barnsley. São parâmetros explícitos na primeira célula, sem modos de alta qualidade.

Os PNGs são gravados em `figuras_fractais/` no diretório de execução. As imagens desta edição estão incorporadas ao notebook. O notebook inclui saídas PNG incorporadas, permitindo leitura sem executar ou buscar arquivos externos. Em Colab, o armazenamento da sessão é temporário: baixe os PNGs antes de encerrar.

## Implementação e custo

Escape e Newton mantêm índices ativos para não atualizar pontos já resolvidos. Os campos usam precisão dupla; o custo máximo é O(pixels × iterações), e memória O(pixels), incluindo temporários. Barnsley é sequencial por dependência de estado e usa histograma de visitas, com custo O(pontos). As cores são sólidas, sem degradês: escape em quatro faixas (1–4, 5–14, 15–34, 35–80 passos); Barnsley em verde único nos pixels visitados; Newton em uma cor por raiz. Preto indica pontos não classificados, ou fundo no Barnsley.

## Evidências e limites

Validado em processo Python novo com NumPy 2.3.5 e Matplotlib 3.10.8. Cinco células de código executadas, cinco figuras inspecionadas, testes de escape conhecido, determinismo, raízes, derivada nula, resíduo final e monotonicidade de escape aprovados. A tentativa de kernel Jupyter local foi bloqueada pelo ambiente (comunicação de rede); esta validação não é apresentada como teste completo do protocolo Jupyter ou teste no Colab. O workflow do repositório pode executar notebooks em kernel disponível.

Ponto que não escapou no orçamento não é certificado como membro do conjunto. Newton mantém pontos sem convergência com rótulo −1. Um zoom extremo requer precisão maior; a malha e as cores não demonstram dimensão fractal ou caos. Todas as referências conceituais e exercícios estão no notebook.

## Galeria

As cinco figuras estão incorporadas nas saídas do [notebook executado](../notebooks/08_fractais_exploracao.ipynb), em cada seção correspondente. Execute-o para exportar os cinco PNGs individuais.
