# Validação

Data da preparação: 31/10/2026. Ambiente local: Python 3.12, NumPy 2.3.5, SciPy 1.17.0 e Matplotlib 3.10.8.

## Resultados obtidos

| Verificação | Resultado local |
| --- | --- |
| Testes numéricos parametrizados | 29 aprovados |
| Esquema e sanitização do acervo | Cinco notebooks aprovados |
| Execução sequencial das células de estudo via IPython | Sete notebooks aprovados em processos novos |
| Células de código executadas nessa edição de estudo | 32 |
| Figuras científicas geradas | 14 SVGs |
| Execução local em kernel Jupyter | Não concluída: sandbox impediu a comunicação do kernel |
| GitHub Actions | Aprovado: 29 testes em Linux/macOS/Windows e sete notebooks via Jupyter |

Os resultados detalhados estão em [validacao-local.json](validacao-local.json). Contadores e saídas textuais locais foram preservados nos notebooks. As figuras ficam em `assets/figuras/`, com galeria ao fim dos roteiros.

## Reproduzir

```sh
python -m pytest -q
python scripts/verificar_acervo.py
python scripts/executar_notebooks.py
```

A alternativa `python scripts/executar_sem_kernel.py` usa IPython em um processo novo por notebook. Ela executa as células e asserções reais, mas não verifica o protocolo ou integração de um kernel Jupyter. O modo usado está identificado na metadata dos arquivos.

## Evidência remota

A [execução 41222104656](https://github.com/luigiscofano/usp-metodos-numericos/actions/runs/41222104656) terminou com sucesso em 31/10/2026 no commit `8ff832d0a208488b9942bc7aeb47c77568002571`, branch `test/execucao-e-ci` (PR #4, posteriormente integrado). Os quatro jobs passaram: testes em Ubuntu 24.04, macOS 15 e Windows, e execução dos sete notebooks via nbclient em kernels Jupyter novos. A verificação do acervo também passou.

[Artefato com sete HTMLs, sete notebooks executados, relatório JSON e 14 figuras](https://github.com/luigiscofano/usp-metodos-numericos/actions/runs/41222104656/artifacts/13050262644), sujeito à retenção de 90 dias do GitHub. O conteúdo numérico e a configuração de CI dessa execução permanecem iguais nos PRs de documentação subsequentes. A limitação do kernel local descrita acima não ocorreu no runner remoto.

O registro estruturado está em [validacao-remota.json](validacao-remota.json).

## O que não foi afirmado

- O acervo não foi corrigido nem executado; suas lacunas permanecem identificadas.
- O sexto arquivo histórico, de Python introdutório, não foi recuperado.
- Não há prova formal de correção ou cobertura de toda entrada possível.
- Benchmarks não são garantias de performance nem critérios de aprovação por tempo.
- Comparação entre integradores é evidência numérica, não validação física de Chua.
- GPS não usa efemérides reais e não foi validado como receptor.
- Não houve avaliação pedagógica com participantes.
- A publicação e os PRs estão registrados em [PUBLICACAO.md](PUBLICACAO.md).
