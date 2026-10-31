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
| GitHub Actions | Publicado; execução remota em acompanhamento |

Os resultados detalhados estão em [validacao-local.json](validacao-local.json). Contadores e saídas textuais locais foram preservados nos notebooks. As figuras ficam em `assets/figuras/`, com galeria ao fim dos roteiros.

## Reproduzir

```sh
python -m pytest -q
python scripts/verificar_acervo.py
python scripts/executar_notebooks.py
```

A alternativa `python scripts/executar_sem_kernel.py` usa IPython em um processo novo por notebook. Ela executa as células e asserções reais, mas não verifica o protocolo ou integração de um kernel Jupyter. O modo usado está identificado na metadata dos arquivos.

O executor padrão com nbclient e o workflow foram preparados para essa verificação em ambiente com kernel funcional. A configuração de um workflow não é evidência de sucesso remoto.

## O que não foi afirmado

- O acervo não foi corrigido nem executado; suas lacunas permanecem identificadas.
- O sexto arquivo histórico, de Python introdutório, não foi recuperado.
- Não há prova formal de correção ou cobertura de toda entrada possível.
- Benchmarks não são garantias de performance nem critérios de aprovação por tempo.
- Comparação entre integradores é evidência numérica, não validação física de Chua.
- GPS não usa efemérides reais e não foi validado como receptor.
- Não houve avaliação pedagógica com participantes.
- A publicação e os PRs estão registrados em [PUBLICACAO.md](PUBLICACAO.md).
