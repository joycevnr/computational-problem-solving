def matriz_coincidencia(M1, M2):
    lista = []
    for i in range(len(M1)):
        linha = []
        for j in range(len(M1[i])):
            if M1[i][j] == M2[i][j]:
                linha.append(M1[i][j])
            else:
                linha.append(0)
        lista.append(linha)
    return lista



M1 = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
M2= [[10, 11, 12],
         [13, 14, 15],
         [ 7,  8,  9]]

M3= [[ 1,  2,  3],
         [13, 14, 15],
         [16, 17, 18]]

M4= [[10, 11, 11]]

M5= [[ 1,  2,  3]]
assert matriz_coincidencia(M4, M5) == [[0,0,0]]

assert matriz_coincidencia(M1, M2) == [[0,0,0],[0,0,0],[7,8,9]]

assert matriz_coincidencia(M1, M3) == [[1,2,3],[0,0,0],[0,0,0]]


# Matriz Coincidência

# Escreva a função <code>matriz_coincidencia(M1, M2)</code> 
# que receba duas matrizes e identifique as
# coincidências entre elas, ou seja, elementos que se encontram na 
# mesma posição (linha e coluna). A função deve retornar uma nova 
# matriz contendo os elementos que coincidem nas suas posições e 0 
# (zero) nas demais posições. Todas as matrizes recebidas pela função 
# e a matriz retornada devem ter o mesmo número de linhas e colunas. 
# Não haverá matrizes vazias. 
