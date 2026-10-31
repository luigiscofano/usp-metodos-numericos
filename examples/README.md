# Exemplos reproduzíveis

[Início](../README.md) · [Como executar](../README.md#como-executar) · [Aprendizagem](../README.md#o-que-desenvolvi-e-aprendi) · [Estado atual](../README.md#estado-atual)

> **Nesta área:** entradas e saídas de demonstração; use os exemplos para reproduzir um cenário antes de alterar o código.

[Início](../README.md) · [Como executar](../README.md#como-executar) · [Aprendizagem](../README.md#o-que-desenvolvi-e-aprendi) · [Estado atual](../README.md#estado-atual)

> **Nesta área:** entradas e saídas de demonstração; use os exemplos para reproduzir um cenário antes de alterar o código.

Os exemplos completos estão nos sete notebooks. Para usar apenas a biblioteca, execute da raiz:

```python
import numpy as np
from numericos.lineares import resolver
from numericos.raizes import newton

A = np.array([[0., 1.], [2., 3.]])
print(resolver(A, [1., 5.]))  # [1., 1.]
r = newton(lambda x: x*x-2, lambda x: 2*x, 1.)
print(r.raiz, r.convergiu, r.motivo)
```

Experimentos estocásticos usam `np.random.default_rng(seed)` local. O GPS utiliza somente dados sintéticos; o exemplo não codifica posição de uma pessoa, dados de navegação reais ou informação de cliente.

---

**Projeto:** [Métodos Numéricos · Sete experimentos reproduzíveis](../README.md). Consulte a raiz para os requisitos e o primeiro comando; este guia aprofunda a área `examples/`.

---

**Projeto:** [Métodos Numéricos · Sete experimentos reproduzíveis](../README.md). Consulte a raiz para os requisitos e o primeiro comando; este guia aprofunda a área `examples/`.
