def busca_matriz(m, e):
    lista = []
    for i in range(len(m)):  # i:linha
        cada_m = m[i]
        for j in range(len(cada_m)):  # j: coluna
            if cada_m[j] == e:  
                lista.append((i, j))  # (linha, coluna)
    print(lista)
    return lista

matriz = [
         [2, 3, 5, 3, 1],
         [3, 2, 1, 5, 6],
         [1, 2, 3, 2, 1],
         ]

# Testes
assert busca_matriz(matriz, 4) == [] 
assert set(busca_matriz(matriz, 3)) == set([(0,1), (0,3), (1,0), (2,2)])


# # Busca Todos em Matriz

# Escreva a função **busca_matriz(m, e)** que busca todas as
# ocorrências do elemento *e* na matriz *m* (representada na forma
# de lista de listas) e que retorna uma lista com os índices
# do elemento e ou uma lista vazia, caso o elemento não
# exista na matriz.

# # Exemplos de asserts

# ````
# matriz = [
#          [2, 3, 5, 3, 1],
#          [3, 2, 1, 5, 6],
#          [1, 2, 3, 2, 1],
#          ]
         
# assert busca_matriz(matriz, 4) == []
# assert set(busca_matriz(matriz, 3)) == set( [(0,1), (0,3), (1,0), (2,2)] )
# ```

