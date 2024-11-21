#falta ajustar

def organiza(array):
    ultimo = array[-1]
    if ultimo < 0 or ultimo == 0 and len(array) > 1:
        i = len(array) - 1
        while array[i-1] > 0 or array[i-1] == 0:
            array[i-1], array[i] = array[i], array[i-1]
            i -= 1 
    #print(array)

l1 = [0, -1]
assert organiza(l1) == None
assert l1 == [0, -1]


l1 = [-2, -4, -1, 0, 0, 10, 1, 2, 7, -20]
assert organiza(l1) == None
assert l1 == [-2, -4, -1, -20, 0, 0, 10, 1, 2, 7]

l2 = [-2, -4, -1, -20, 0, 0, 10, 1, 2, 7, 0]
assert organiza(l2) == None
assert l2 == [-2, -4, -1, -20, 0, 0, 0, 10, 1, 2, 7]

l3 = [-2, -4, -1, -20, 0, 0, 0, 10, 1, 2, 7, 4]
assert organiza(l3) == None
assert l3 == [-2, -4, -1, -20, 0, 0, 0, 10, 1, 2, 7, 4]

# # Só o Último Fora de Lugar?

# Considere um array de inteiros idealmente organizado em 3 partes: 
# a primeira parte contém apenas números negativos, na parte central 
# só ocorrência de zeros e na terceira parte só números positivos. 
# As partes individuais não estão necessariamente ordenadas. 

# Escreva a função `organiza(array)` que recebe um array que possivelmente
# está organizado seguindo a distribuição definida acima. A dúvida é apenas
# no último valor do array que pode ou não furar a regra de distribuição de
# valores no arrayi. Essa função organiza o array, mantendo a ordem relativa 
# dos valores do array, mas garantindo a distribuição dos valores nas 3 partes 
# como definido acima.

# Por exemplo, considere o array

# ```
# [-2, -4, -1, 0, 0, 10, 1, 2, 7, -20]
# ```

# O último elemento está fora de posição,ferindo a regra das 3 partes. Aplicando
# a função `organiza` nesse array, a nova configuração do array seria:

# ```
# [-2, -4, -1, -20, 0, 0, 10, 1, 2, 7]
# ```

# Obviamente se o último elemento não fere a regra, a função `organiza` não vai 
# alterar o array original.


# ## Atenção

# Considerar apenas a API básica de arrays. Não é permitido adicionar, remover
# elementos do array e nem utilizar lista auxiliar.

# A função deve executar em tempo linear.

# <small>Jorge Figueiredo</small>