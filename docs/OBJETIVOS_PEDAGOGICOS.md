# Objetivos pedagógicos

**Compreender o mecanismo de uma aproximação e construir evidência de que ela é adequada ao problema.** O foco não é apenas obter uma tabela ou um gráfico, mas explicar hipóteses, critérios de parada, sensibilidade e custo.

## Competências e evidências

| Competência | Atividade concreta | Evidência esperada |
| --- | --- | --- |
| Usar arrays, funções e vetorização | Reproduzir f(x) por laço e expressão vetorizada | Mesmos valores, shapes explicados e máscara interpretada |
| Distinguir erro absoluto e relativo | Comparar aproximação de √2 e caso de referência zero | Métrica escolhida e divisão por zero evitada |
| Interpretar convergência de Newton | Resolver raiz simples, múltipla e um ciclo | Iteradas, resíduos e motivo de parada |
| Ler bacias de atração criticamente | Variar malha e limite de iterações para z³−1 | Pontos sem convergência mantidos explícitos |
| Entender ponto flutuante | Comparar subtração direta e racionalização | Curva de erro com interpretação do cancelamento |
| Justificar pivotamento | Resolver matriz com pivô inicial zero/pequeno | PA=LU e solução conhecida reproduzidos |
| Separar resíduo e erro | Resolver sistemas de Hilbert com x exato conhecido | Condicionamento, resíduo e erro apresentados separadamente |
| Comparar transformadas de forma justa | Executar DFT, FFT e NumPy na mesma convenção | Coeficientes consistentes e inversa reconstruindo entrada |
| Investigar amostragem | Mostrar alias de um sinal de 27 Hz amostrado a 32 Hz | Explicação da ambiguidade dos dados amostrados |
| Escolher nós de interpolação | Comparar Runge com nós uniformes e de Chebyshev | Erro máximo medido, não inferido só da figura |
| Distinguir aproximação global e por trechos | Comparar polinômio e spline natural | Condição de contorno e conjunto de nós explicitados |
| Estimar ordem de integração | Reduzir h pela metade em u′=u | Razões de erro compatíveis com ordens 1, 2 e 4 |
| Separar estabilidade de dinâmica física | Executar Euler em u′=−20u com dois passos | Crescimento espúrio identificado como numérico |
| Interpretar simulação de Chua | Refinar passo e comparar janela curta com DOP853 | Diferenças por componente e limites físicos registrados |
| Modelar um sistema não linear | Estimar ECEF e viés de relógio com dados sintéticos | Jacobiano, posto, resíduos e erro de posição |
| Produzir trabalho reproduzível | Reexecutar em processo/kernel novo | Ambiente, seeds, código e critério de aprovação disponíveis |

## Sequência sugerida

1. **Fundamentos:** notebook 01 e métricas de erro.
2. **Convergência:** notebook 02, sem omitir casos de falha.
3. **Álgebra linear:** notebook 03, com identidade PA=LU e reescala.
4. **Representação e aproximação:** notebooks 04 e 05.
5. **Evolução temporal:** notebook 06, começando pelo caso com solução analítica.
6. **Integração de conceitos:** notebook 07, distinguindo modelo simplificado e receptor real.

## Propostas de avaliação

| Dimensão | Critério |
| --- | --- |
| Correção matemática | Fórmulas, convenções e unidades consistentes |
| Implementação | Entradas válidas, falhas sinalizadas e preservação de dados |
| Experimento | Variação controlada de um parâmetro e referência adequada |
| Interpretação | Conclusão sustentada por medidas e reconhecimento dos limites |
| Reprodutibilidade | Código, dependências, seeds e execução do início ao fim |
| Comunicação | Separação entre material recuperado e complemento novo |

## Perguntas para discussão

- Um resíduo pequeno pode coexistir com erro grande? Mostre um caso.
- Como uma normalização inconsistente cria um “erro” inexistente entre DFT e FFT?
- Por que um interpolador deve devolver diretamente o dado quando avaliado num nó?
- Por que a ordem observada pode deixar de aparecer com h muito pequeno?
- Qual a diferença entre divergência numérica e divergência de trajetórias em um sistema sensível?
- O que muda ao ter mais observações do que incógnitas no GPS sintético?

Essas atividades são propostas de estudo desta edição. Não foi realizado experimento com participantes nem atribuída uma nota acadêmica ao titular do repositório.
