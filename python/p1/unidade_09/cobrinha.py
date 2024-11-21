def cobrinha(M):
    impares = []
    for i in range(len(M)):
        if (i + 1) % 2 != 0:
            for j in range(len(M[i])):
                if M[i][j] % 2 != 0:
                    impares.append(M[i][j])
        else:
            for k in range(len(M[i])-1, -1, -1):
                if M[i][k] % 2 != 0:
                    impares.append(M[i][k])
    print(impares)
    return impares


M = [[1,2,3],
     [4,5,6],
     [7,8,9]]

assert cobrinha(M) == [1, 3, 5, 7, 9]

M = [[1,4],
     [3,1],
     [2,7],
     [0,9]]

assert cobrinha(M) == [1, 1, 3, 7, 9]

# # Cobrinha

# Escreva a função `cobrinha(M)` que monta uma lista de inteiros
# ímpares gerada a partir do caminhamento em  vai e vem de uma
# matriz de inteiros. O caminhamento em vai e vem incia na primeira
# linha do sentido da esquerda pra direita e inverte na linha
# seguinte. A lista de ímpares mantem a ordem em que os inteiros
# ímapres da matriz original foram visitados.

# ## Semantica da Função

# Espera-se que a função não tenha efeito colateral e retorne uma
# lista com os inteiros ímpares mantendo a ordem de ocorrência
# deles no caminhamento vai e vem.