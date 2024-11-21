def diagonais(M):
    diagonal_p = []  # Diagonal principal
    diagonal_s = []  # Diagonal secundária
    n = len(M)  # Tamanho da matriz (assumindo que é quadrada)
    
    for i in range(n):
        diagonal_p.append(M[i][i])           # Diagonal principal: mesma linha e coluna (i, i)
        diagonal_s.append(M[i][n - 1 - i])   # Diagonal secundária: (i, n-1-i)
    
    return [diagonal_p, diagonal_s]  # Retorna as duas diagonais como uma matriz

M = [[1,2,3],
     [4,5,6],
     [7,8,9]]

assert diagonais(M) == [[1,5,9],[3,5,7]]

# # Diagonais

# Escreva a função `diagonais(M)` que retorna uma matriz cuja 
# primeira linha contem os valores da diagonal principal de M, enquanto a segunda linha contém
# os valores da diagonal secundária de M, sendo M uma matriz quadrada.

