def inserir(lista, elem, posicao):
    lista.append(elem)
    i = len(lista) -1
    while i != posicao:
        lista[i-1], lista[i] = lista[i], lista[i-1]
        i -= 1


def na_posicao(lista, a_inserir):
    for par in a_inserir:
        inserir(lista, par[0], par[1])



l = [10, 20, 30]
a_inserir = [(5, 1), (-2, 4), (0, 0)]
#print(na_posicao(l, a_inserir))
assert na_posicao(l, a_inserir) == None
print(l)
assert l == [0, 10, 5, 20, 30, -2]


# Insere na Posição Indicada

# Escreva a função `na_posicao(lista, a_inserir)` que recebe
# uma lista de números inteiros e uma sequencia de pares `(num, pos)`
# e insere na lista cada `num` da sequencia na posição `pos`. A função
# `na_posicao()` retorna `None` e altera a lista original de acordo com
# os números e posições da sequencia.

# *Dica:* para acessar os elementos
# de um par, utilize o mesmo conceito de indexação utilizado para acessar elementos
# de uma lista. Ou seja, a posição `0` corresponde ao primeiro elemento
# do par e a posição `1` o segundo elemento do par.

# ## Exemplo

#     l = [10, 20, 30]
#     a_inserir = [(5, 1), (-2, 4), (0, 0)]
#     assert na_posicao(l, a_inserir) == None
#     assert l == [0, 10, 5, 20, 30, -2]

# ## Atenção

# Assuma que a sequencia contém apenas pares com posições válidas.

# Para inserir elementos na lista só é permitido utilizar `append`. Não
# é permitido utilizar nenhuma outra função de listas para inserir elementos
# na lista.
