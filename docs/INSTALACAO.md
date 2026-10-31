# Instalação e reprodução

## Ambiente recomendado para esta edição

Python 3.12, com dependências diretas fixadas em `requirements.txt`. Os módulos científicos foram testados localmente com NumPy 2.3.5, SciPy 1.17.0 e Matplotlib 3.10.8. Dependências transitivas podem variar; o arquivo não é um lock completo.

## Preparar

```sh
python -m venv .venv
```

Ative o ambiente:

- Linux/macOS: `source .venv/bin/activate`
- Windows PowerShell: `.venv\Scripts\Activate.ps1`

Depois:

```sh
python -m pip install -r requirements.txt
python -m ipykernel install --user --name python3 --display-name "Python 3"
python -m pytest -q
python scripts/verificar_acervo.py
```

A biblioteca pode ser importada a partir da raiz. Para instalá-la em modo editável, `python -m pip install -e .`; use `requirements.txt` para obter o conjunto completo de ferramentas dos notebooks.

## Executar os sete roteiros em kernel novo

```sh
python scripts/executar_notebooks.py
```

O script usa `nbclient`, não aceita erros de célula e grava em `build/`:

- Um `.ipynb` executado por roteiro.
- Uma versão HTML por roteiro.
- Um JSON com resultados e tempo observado.

As figuras são geradas em `assets/figuras/`. O backend Agg dispensa janela gráfica. A pasta `acervo/` é validada quanto a esquema/sanitização, mas não executada.

## Abrir interativamente

Use um editor compatível com Jupyter, selecionando o ambiente Python preparado. Execute a partir da raiz ou da pasta `notebooks/`. Os roteiros localizam o pacote do repositório e não dependem de um Drive montado.

JupyterLab não é uma dependência obrigatória do exportador; instale-o à parte caso deseje essa interface específica. A execução automatizada usa apenas kernel e nbclient.

## Alternativa sem servidor/kernel Jupyter

```sh
python scripts/executar_sem_kernel.py
```

Esse modo executa células com IPython, em um processo novo por notebook. Foi usado na verificação local porque a sandbox não permitiu iniciar a comunicação do kernel. Não prova integração com o protocolo Jupyter; essa verificação pertence ao executor padrão e ao CI remoto quando disponível.

Para atualizar contadores e outputs textuais versionados, acrescente `--atualizar` a um executor, examine o diff e confirme que as figuras e conclusões ainda correspondem ao experimento.

## Problemas frequentes

| Mensagem/sintoma | Diagnóstico |
| --- | --- |
| `No such kernel named python3` | Registre o kernel no ambiente usado pelo script |
| `No module named numericos` | Execute da raiz ou abra notebook em raiz/notebooks |
| Processo do kernel não inicia em sandbox | Use a alternativa sem kernel e registre a limitação |
| DFT rejeita N grande | Limite intencional de memória; use FFT para tamanhos maiores |
| FFT rejeita N=3 | Implementação didática radix-2 exige potência de dois |
| EDO diverge | Revise passo, estabilidade e modelo; não ignore avisos/asserções |
| Figura muda ligeiramente entre máquinas | Fontes e renderização podem variar; compare critérios numéricos |
