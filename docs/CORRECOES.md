# Problemas encontrados e decisões da edição

O acervo é preservado com suas limitações. As soluções abaixo estão na biblioteca e nos roteiros de estudo, sem alterar silenciosamente o código histórico.

| Achado no material recuperado | Consequência | Tratamento na edição de estudo |
| --- | --- | --- |
| `np.math.factorial` na interpolação | Saída histórica registra AttributeError com NumPy atual | Uso explícito de `math.factorial` |
| DFT dividida por N e FFT sem essa divisão | Diferença de escala confundida com erro | Mesma convenção de NumPy: direta sem escala, inversa com 1/N |
| `tools.display_dataframe_to_user` no FFT | Comando não disponível em Python/Colab comum | Saídas locais de tabela e gráficos, sem serviço proprietário |
| DFT densa até N=32768 | Matriz complex128 exige 16 GiB, além dos temporários | Benchmark pequeno e limite explícito no método denso |
| LU histórica sem pivotamento | Falha com pivô zero ou pequeno | PLU com pivotamento parcial e teste PA=LU |
| Retorno de `np.empty` em alguns caminhos de falha | Valores não inicializados podem parecer solução | Exceções e diagnósticos explícitos |
| Células e respostas em branco no Chua | Não se pode afirmar que o EP estava completo | Roteiro novo com Euler, Heun, RK4, pêndulo e sistema de Chua |
| Identificador de exemplo em Chua | Não correspondia ao titular do portfólio | Número USP autorizado do titular, com nota de alteração |
| Imagens incorporadas de terceiros | Procedência visual distinta do código do aluno | Omissão no acervo público e geração de figuras novas |
| Interrupção da recuperação de Python introdutório | Destino histórico não recuperado | Substituição nova identificada, sem fingir recuperação |

## Critérios numéricos

- Newton só certifica convergência por resíduo e registra falhas.
- Bacias mantêm explicitamente os pontos não convergidos.
- PLU preserva as entradas e testa pivôs em escala relativa.
- Interpolação retorna o dado no nó e rejeita nós repetidos.
- FFT testa entrada complexa, convenção e inversa.
- EDO confronta ordem e estabilidade em problemas com solução conhecida.
- Chua foi refinado de 8.000 para 32.000 passos na janela de 8 ms para atender ao critério por componente frente a DOP853. Não se afrouxou o critério para ocultar a falha inicial.
- GPS é identificado como extensão sintética e rejeita geometria sem posto suficiente.
