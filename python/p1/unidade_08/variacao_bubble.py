def variacao_bubble(vetor, ini, fim):
    trocas = 0  # Contador de trocas
    # Loop para comparar elementos simétricos
    for i in range(ini, (fim + ini) // 2):  # Para garantir que não ultrapasse o limite
        # Índice do elemento simétrico
        simetrico = fim - 1 - (i - ini)  
        # Se o elemento atual é maior que o simétrico, troque
        if vetor[i] > vetor[simetrico]:
            vetor[i], vetor[simetrico] = vetor[simetrico], vetor[i]  # Troca
            trocas += 1  # Incrementa o contador de trocas
    return trocas

# Exemplos de uso
vetor1 = [6, 9, 2, 3, 1, 4]
assert variacao_bubble(vetor1, 0, 6) == 2
assert vetor1 == [4, 1, 2, 3, 9, 6]

vetor2 = [8, 6, 9, 2, 3, 1, 4, 0, 7, 4]
assert variacao_bubble(vetor2, 1, 7) == 2
assert vetor2 == [8, 4, 1, 2, 3, 9, 6, 0, 7, 4]

# Variação Bubble

# Um estudante de programação decidiu fazer experimentos com
# algumas variações do _bubblesort_. Uma das idéias que teve
# foi a de ao invés de comparar e trocar elementos
# consecutivos do vetor, fazer essa operação com elementos
# simétricos de uma parte do vetor. Por exemplo, se em alguma
# etapa essa parte for o vetor inteiro, devem ser comparados e
# trocados, se necessário, o primeiro e o último elementos do
# vetor; em seguida, o segundo e o penúltimo elementos; e
# assim por diante.

# Pede-se que você implemente a função `variacao_bubble(vetor,
# ini, fim)` que executa um passo completo dessa variação do
# algoritmo para o trecho do vetor delimitado pelos índices
# `ini` e `fim`.

# ## Semântica da função

# A função deve operar sobre uma lista, tratando-a como um
# _array_. Ou seja, nenhuma operação de alteração estrutural
# da lista pode ser realizada, tais como inserções, remoções,
# slices, etc. Apenas a atribuição de valores é possível. A
# função também deve retornar o número de trocas realizadas no
# passo. Veja um primeiro exemplo abaixo.

# ```
# vetor = [6, 9, 2, 3, 1, 4]
# assert variacao_bubble(vetor, 0, 6) == 2
# assert vetor == [4, 1, 2, 3, 9, 6]
# ```

# Os parâmetros `ini` e `fim` indicam os limites, usando a
# semântica tipicamente usada em python para trechos de
# sequências (_slices_ e _ranges_, por exemplo). Ou seja, o
# parâmetro `ini` indica o índice inicial e o parâmetro `fim`
# indica o final do trecho, mas não está incluído. Observe que
# a parte do vetor que fica fora dos limites indicados pelos
# parâmetros `ini` e `fim` não deve ser alterada. Veja isso no
# segundo exemplo abaixo.