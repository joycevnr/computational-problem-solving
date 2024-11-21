def matriz_menor(M1, M2):
    matriz_resultado = []  # Matriz que vai armazenar os menores valores
    
    # Percorre cada linha
    for i in range(len(M1)):
        linha_resultado = []  # Lista para armazenar os menores valores da linha
        
        # Percorre cada coluna dentro da linha
        for j in range(len(M1[i])):
            if M1[i][j] < M2[i][j]:
                linha_resultado.append(M1[i][j])  # Adiciona o menor valor de M1
            else:
                linha_resultado.append(M2[i][j])  # Adiciona o menor valor de M2
        
        matriz_resultado.append(linha_resultado)  # Adiciona a linha completa à matriz resultado
    
    return matriz_resultado  # Retorna a matriz com os menores valores

# Testes
M1 = [[1,2,3],
      [13,14,15],
      [7,8,9]]
         
M2 = [[10,11,12],
      [4,5,6],
      [7,8,9]]
         
M3 = [[1,2,3],
      [0,0,0],
      [7,8,9]]

# Saída esperada: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz_menor(M1, M2))

# Testes com assert
assert matriz_menor(M1, M2) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
assert matriz_menor(M1, M3) == [[1, 2, 3], [0, 0, 0], [7, 8, 9]]
