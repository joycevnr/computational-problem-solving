#QUESTÃO COMPLEXA

def soma_moldura(m, k):
    n = len(m)  # Obtém o tamanho da matriz
    
    # Verifica se a moldura k é válida
    if k >= n // 2:
        return 0  # Retorna 0 se não houver moldura k
    
    # Define os limites da submatriz para a moldura k
    topo = k
    fundo = n - k - 1
    esquerda = k
    direita = n - k - 1
    
    # Inicializa a soma
    soma = 0
    
    # Soma os elementos da parte superior da moldura
    for j in range(esquerda, direita + 1):
        soma += m[topo][j]
    
    # Soma os elementos da parte direita da moldura
    for i in range(topo + 1, fundo):
        soma += m[i][direita]
    
    # Soma os elementos da parte inferior da moldura
    if fundo > topo:  # Evita duplicação em matrizes 1x1
        for j in range(direita, esquerda - 1, -1):
            soma += m[fundo][j]
    
    # Soma os elementos da parte esquerda da moldura
    if esquerda < direita:  # Evita duplicação em matrizes 1x1
        for i in range(fundo - 1, topo, -1):
            soma += m[i][esquerda]
    
    return soma  # Retorna a soma total

# Exemplo de uso e testes
M = [[1,  2,  3,  4],
     [5,  6,  7,  8],
     [9, 10, 11, 12],
     [14, 15, 16, 17]]

# Testes
assert soma_moldura(M, 0) == 106  # Soma da moldura 0
assert soma_moldura(M, 1) == 34   # Soma da moldura 1


# # Molduras em Matriz Quadrada

# Matriz quadrada é um tipo especial de matriz que possui o mesmo número de linhas e o 
# mesmo de colunas.  Considere a matriz quadrada  M abaixo de dimensão 4 (representada 
# como lista de listas).

# ```
# M = [[1,  2,  3,  4 ],
#      [5,  6,  7,  8 ],
#      [9,  10, 11, 12],
#      [14, 15, 16, 17]]
# ```

# Definimos `moldura_0` ou moldura nível 0 de uma matriz quadrada como sendo os 
# elementos que compõem as bordas dessa matriz. No exemplo acima, a `moldura_0` 
# seria formada pelos elementos 1, 2, 3, 4, 8, 12, 17, 16, 15, 14, 9 e 5. A `moldura_1` de M
# é formada pelos elementos que margeiam os elementos da `moldura_0`. Assim, nesse 
# exemplo, a `moldura_1` seria formada pelos seguintes elementos 6, 7, 11 e 10. Para 
# ser considerado moldura, é necessário ter pelo menos 4 elementos.

# Se considerarmos uma matriz quadrada genérica de dimensão `n`, em que `n >= 2`, é 
# possível ter `n / 2` molduras. Por exemplo, para uma matriz quadrada de dimensão 6, 
# poderíamos ter 3 níveis de moldura (`moldura_0`, `moldura_1` e `moldura_2`).

# Escreva a função `soma_moldura(m, k)` que recebe uma matriz quadrada `m` e retorna 
# a soma dos elementos da `k`-ésima moldura. 