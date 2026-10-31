# Biblioteca didática

[Início](../README.md) · [Como executar](../README.md#como-executar) · [Aprendizagem](../README.md#o-que-desenvolvi-e-aprendi) · [Estado atual](../README.md#estado-atual)

> **Nesta área:** métodos reutilizáveis por tema, que apoiam os notebooks sem exigir a execução de todos os roteiros.

[Início](../README.md) · [Como executar](../README.md#como-executar) · [Aprendizagem](../README.md#o-que-desenvolvi-e-aprendi) · [Estado atual](../README.md#estado-atual)

> **Nesta área:** métodos reutilizáveis por tema, que apoiam os notebooks sem exigir a execução de todos os roteiros.

Os módulos desta pasta foram implementados nesta edição e são usados pelos notebooks de estudo. Não dependem dos arquivos do acervo.

| Módulo | API principal | Decisão importante |
| --- | --- | --- |
| [raizes.py](raizes.py) | `newton`, `bacias_newton` | Retorna motivo de parada e preserva pontos não convergidos |
| [lineares.py](lineares.py) | `fatorar_plu`, `resolver`, `gauss_reduzido` | Convenção PA=LU; pivotamento parcial; entradas preservadas |
| [interpolacao.py](interpolacao.py) | Newton e baricêntrica | Nós distintos; retorno exato do dado no nó |
| [fourier.py](fourier.py) | `dft`, `fft`, `ifft` | Direta sem fator 1/N; inversa com 1/N; radix-2 |
| [edo.py](edo.py) | `integrar`, `circuito_chua` | Passo fixo, Euler/Heun/RK4; derivada com forma verificada |
| [gps.py](gps.py) | Gauss–Newton e ECEF/geodésicas | Viés em metros, mínimos quadrados sem equações normais |

## Contratos e hipóteses

- As entradas devem ser finitas e de dimensões compatíveis. Casos claramente inválidos geram exceções em vez de vetores não inicializados.
- PLU trabalha com matrizes reais quadradas e um vetor b; o limiar de pivô depende da escala de A e pode rejeitar problemas numericamente singulares.
- Interpolação recebe valores reais e nós distintos. Pesos são reescalados, mas não há garantia de estabilidade para qualquer quantidade/distribuição de nós ou extrapolação extrema.
- Newton recebe funções escalares reais/complexas; um limiar absoluto de derivada pode requerer reescala.
- FFT é radix-2; DFT densa aceita no máximo 2048 pontos para limitar memória.
- EDO exige intervalo crescente, número positivo de passos e estado escalar/vetor. Não implementa adaptação de passo ou eventos.
- GPS usa pseudodistâncias positivas e ao menos quatro observações com Jacobiano de posto quatro. Gauss–Newton pode falhar para chutes ou geometrias inadequadas.

Veja [métodos e complexidade](../docs/METODOS.md) e [testes](../tests/README.md).

---

**Projeto:** [Métodos Numéricos · Sete experimentos reproduzíveis](../README.md). Consulte a raiz para os requisitos e o primeiro comando; este guia aprofunda a área `numericos/`.

---

**Projeto:** [Métodos Numéricos · Sete experimentos reproduzíveis](../README.md). Consulte a raiz para os requisitos e o primeiro comando; este guia aprofunda a área `numericos/`.
