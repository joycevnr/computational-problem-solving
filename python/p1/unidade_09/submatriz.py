def submatriz(A, p, q, r, s):
    # Verificar se os índices são válidos
    if p < 0 or q < 0 or r >= len(A) or s >= len(A[0]) or p > r or q > s:
        return None
    
    # Criar a submatriz
    resultado = []
    for i in range(p, r + 1):  # Percorre as linhas de p até r
        linha = []  # Inicializa uma nova linha
        for j in range(q, s + 1):  # Percorre as colunas de q até s
            linha.append(A[i][j])  # Adiciona o elemento à nova linha
        resultado.append(linha)  # Adiciona a linha à submatriz

    print(resultado)
    return resultado

# Testes
M = [[11, 12, 13, 14, 15, 16],
     [21, 22, 23, 24, 25, 26],
     [31, 32, 33, 34, 35, 36],
     [41, 42, 43, 44, 45, 46],
     [51, 52, 53, 54, 55, 56],
     [61, 62, 63, 64, 65, 66]]

assert submatriz(M, 1, 3, 3, 4) == [[24, 25],
                                    [34, 35],
                                    [44, 45]]

assert submatriz(M, 2, 3, 5, 7) == None

# # Submatriz

# Escreva a função `submatriz(A, p, q, r, s)` que recebe a
# amatriz A (m x n) e retorna uma submatriz contendo o bloco
# de dados delimitado pelos índices `p` e `q` (canto superior
# esquerdo) e `r` e `s` (canto inferior direito). 

# ## Condição de existência

# Para que a submatriz especificada esteja bem definida é
# necessário que todos os índices (`p`, `q`, `r` e `s`) sejam
# válidos para a matriz recebida e ainda que `p <= r <= m`, que
# `q <= s <= n`. Caso isso não ocorra, a submatriz não está
# definida.

# ## Especificação da função

# Se a submatriz especificada for bem definida a função deve
# retornar uma matriz que a represente. Caso contrário, a
# função deve retornar `None`. Em qualquer caso, a função não
# deve ter qualquer efeito sobre a matriz original. Veja os
# asserts no exemplo abaixo.

# Leia o arquivo de teste para ver um `assert` que exemplifica o
# uso da função.
