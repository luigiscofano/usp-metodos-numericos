# Apresentação — roteiro de 8 a 10 minutos

## 1. Contexto e procedência — 1 minuto

Apresentar cinco notebooks recuperados, os sete roteiros de estudo e a distinção entre materiais da disciplina, respostas recuperadas e complementos desta edição. Informar que um título histórico introdutório continua com recuperação pendente.

## 2. Objetivo pedagógico — 1 minuto

Explicar a pergunta central: “Como saber se uma aproximação é confiável?”. Mostrar erro, resíduo, convergência, estabilidade, condicionamento e custo como critérios distintos.

## 3. Newton — 1 minuto

Abrir o notebook 02, mostrar tabela de resíduos, ciclo 0↔1 e bacias de atração. Identificar pontos não convergidos sem atribuir uma raiz por proximidade visual.

## 4. Álgebra linear e Fourier — 2 minutos

Mostrar PA=LU com pivotamento e o exemplo de Hilbert. Em seguida, demonstrar que DFT/FFT precisam usar a mesma normalização antes da comparação. Explicar por que uma DFT densa de 32768 pontos não é uma escolha adequada para um notebook comum.

## 5. Interpolação e EDO — 2 minutos

Mostrar Runge com nós uniformes e de Chebyshev. Comparar ordem de Euler, Heun e RK4 e o exemplo de instabilidade de Euler. Explicar por que um gráfico de Chua exige refinamento e comparação quantitativa.

## 6. Integração de conceitos — 1 minuto

Abrir GPS sintético: quatro incógnitas, Jacobiano e mínimos quadrados. Distinguir resíduo de erro de posição e deixar claro que os dados não são reais.

## 7. Evidências e limites — 1 minuto

```sh
python -m pytest -q
python scripts/verificar_acervo.py
python scripts/executar_notebooks.py
```

Apresentar o modo efetivamente executado no ambiente e a situação do CI. Não afirmar aprovação de kernel Jupyter ou GitHub Actions sem uma execução correspondente. Encerrar com uma pergunta: qual hipótese falharia se o tamanho, a escala ou o ruído fossem aumentados?
