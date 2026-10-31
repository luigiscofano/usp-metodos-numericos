# Testes numéricos

[Início](../README.md) · [Como executar](../README.md#como-executar) · [Aprendizagem](../README.md#o-que-desenvolvi-e-aprendi) · [Estado atual](../README.md#estado-atual)

> **Nesta área:** testes e seus critérios de aprovação; um resultado deve ser interpretado dentro da cobertura documentada.

[Início](../README.md) · [Como executar](../README.md#como-executar) · [Aprendizagem](../README.md#o-que-desenvolvi-e-aprendi) · [Estado atual](../README.md#estado-atual)

> **Nesta área:** testes e seus critérios de aprovação; um resultado deve ser interpretado dentro da cobertura documentada.

Execute `python -m pytest -q` a partir da raiz. São **29 casos parametrizados** na suíte atual.

| Família | Oráculo e casos de borda |
| --- | --- |
| Newton | √2 e raiz complexa conhecidas; derivada nula e limite de iterações |
| Bacias | Três raízes de z³−1 e origem não classificada |
| PLU | PA=LU; soluções conhecidas; NumPy; preservação das entradas; matriz singular, pivô zero e reescala |
| Precisão reduzida | Matriz com pivô inicial pequeno e efeito de pivotamento |
| Interpolação | Reprodução de cúbica, avaliação nos nós, um nó e rejeição de repetição |
| Fourier | Vetores complexos; comparação com NumPy; ida/volta; potência de dois e limite de DFT |
| EDO | Razões de erro de Euler/Heun/RK4; oscilador com solução conhecida; forma da derivada |
| Chua | Continuidade da corrente por trechos, equilíbrio e finitude em janela curta |
| Geodesia/GPS | Ida/volta em posições sintéticas, polos, referência exata e geometria degenerada |

Asserções dentro dos notebooks verificam seus próprios experimentos. O teste de ordem usa razões com margens, não tempos de execução. A suíte não faz prova formal de correção nem cobre todas as entradas possíveis.

---

**Projeto:** [Métodos Numéricos · Sete experimentos reproduzíveis](../README.md). Consulte a raiz para os requisitos e o primeiro comando; este guia aprofunda a área `tests/`.

---

**Projeto:** [Métodos Numéricos · Sete experimentos reproduzíveis](../README.md). Consulte a raiz para os requisitos e o primeiro comando; este guia aprofunda a área `tests/`.
