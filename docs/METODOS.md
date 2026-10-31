# Métodos, hipóteses e custo

## Erro, resíduo e condicionamento

Para uma solução conhecida x*, o erro é x−x*. Em Ax=b, o resíduo é Ax−b. O módulo reporta também

$$\eta=\frac{\|Ax-b\|_\infty}{\|A\|_\infty\|x\|_\infty+\|b\|_\infty}.$$

Um resíduo pequeno não implica erro de solução pequeno sem considerar o condicionamento. As comparações com Hilbert mostram essas quantidades separadamente. O arredondamento decimal simulado não é apresentado como implementação de um formato IEEE reduzido.

## Newton para raízes

$$x_{k+1}=x_k-\frac{f(x_k)}{f'(x_k)}.$$

Para raiz simples e chute suficientemente próximo, sob regularidade adequada, a convergência local pode ser quadrática. Raízes múltiplas e ciclos mostram limites dessa expectativa. O critério principal é resíduo; derivada pequena, valor não finito, estagnação e limite de iterações têm diagnósticos próprios.

O limiar de derivada é absoluto e pode precisar ser reescalado. A classificação de bacias exige resíduo pequeno; pontos não certificados continuam com rótulo −1.

## Eliminação e PLU

O pivotamento parcial seleciona o maior módulo disponível na coluna. A convenção é **PA=LU**. Ao trocar duas linhas, a parte já construída de L também é trocada. A solução usa substituições triangulares.

O algoritmo didático é O(n³) em tempo e O(n²) em memória. Não substitui uma rotina LAPACK otimizada; o objetivo é tornar a construção e seus testes legíveis.

## Interpolação

A forma de Newton usa diferenças divididas e avaliação aninhada, com construção O(n²) e avaliação O(n) por ponto. A forma baricêntrica é

$$p(x)=\frac{\sum_j w_jy_j/(x-x_j)}{\sum_j w_j/(x-x_j)},\qquad x\ne x_j,$$

com retorno direto de yj quando x=xj. Os pesos são reescalados por um fator comum, que não altera o polinômio. Nós repetidos são rejeitados.

Nós de Chebyshev-Lobatto incluem as extremidades. A spline natural usada na comparação impõe segunda derivada zero nas extremidades. A escolha do conjunto de nós e da condição de contorno faz parte do experimento, e extrapolação merece análise própria.

## Fourier

$$X_k=\sum_{j=0}^{N-1}x_j e^{-2\pi i jk/N},\qquad
x_j=\frac1N\sum_{k=0}^{N-1}X_k e^{2\pi i jk/N}.$$

A DFT densa tem tempo e memória O(N²). Uma matriz N=32768 em complex128 ocupa 16 GiB, sem temporários; por isso o módulo limita N a 2048, e os benchmarks usam N≤512. A FFT recursiva radix-2 tem tempo O(N log N), mas overhead Python pode ser significativo para N pequeno.

A convenção direta/inversa é a padrão `backward` do NumPy. Amostragem e aliasing são estudados separadamente da implementação. Não se infere frequência analógica única a partir de amostras ambíguas.

## EDO

Para u′=f(t,u), Euler usa `u+h f(t,u)`, Heun usa uma média de inclinações inicial/predita e RK4 combina quatro estágios. As ordens globais esperadas, sob as hipóteses usuais, são 1, 2 e 4. Passo fixo não implica estabilidade.

O teste u′=λu permite analisar o fator de amplificação de Euler, 1+hλ. O pêndulo usa energia específica como diagnóstico em janela finita. RK4 não é simplético.

Chua usa o modelo elétrico e parâmetros do material recuperado, com variáveis em SI. A curva de corrente é contínua por trechos, mas tem mudanças de inclinação; não se assume a mesma ordem observada de um problema inteiramente suave em qualquer regime. Refinamento e referência adaptativa são comparações numéricas, não validação em bancada.

## GPS sintético

$$\rho_i=\|r-s_i\|+b.$$

A derivada em relação a r é `(r−sᵢ)/||r−sᵢ||`, e em relação ao viés em metros é 1. A cada passo, `lstsq` resolve o incremento sem formar JᵀJ. A implementação verifica posto quatro e limita iterações.

A transformação ECEF/geodésica usa o elipsoide WGS84. O exemplo omite efemérides, correções atmosféricas, relógio de satélite, rotação durante propagação, relatividade e multicaminho. Não é um receptor real ou ferramenta de navegação.
