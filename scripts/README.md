# Execução, validação e exportação

| Script | Uso |
| --- | --- |
| `verificar_acervo.py` | Valida formato, inventário e ausência de outputs/imagens/links privados no acervo |
| `executar_notebooks.py` | Executa cada roteiro em kernel Jupyter novo; exporta HTML e ipynb para build/ |
| `executar_sem_kernel.py` | Alternativa local: executa células com IPython em processo novo, sem servidor Jupyter |

Ambos os executores param a aprovação de um notebook quando uma célula falha e registram resultados em JSON. Não usam `allow_errors=True` para transformar erro em aprovação.

`--atualizar` substitui as saídas textuais e os contadores dos arquivos de estudo depois da execução, mantendo as imagens em SVG na pasta de figuras. Examine o diff antes de versionar. O acervo histórico não é alterado por esses executores.

O modo sem kernel foi incluído porque a sandbox local não permitiu iniciar a comunicação do kernel Jupyter. Ele não é descrito como equivalente a um teste de integração do protocolo Jupyter. O workflow remoto usa o executor com kernel.
