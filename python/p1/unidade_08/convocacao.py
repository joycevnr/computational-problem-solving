def atualiza_convocados(lista, novo_convocado):
    nome, posicao = novo_convocado
    inserido = False

    # Percorre a lista para encontrar a posição correta
    for i in range(len(lista)):
        # Verifica se devemos inserir o novo convocado aqui
        if (lista[i][1] > posicao) or (lista[i][1] == posicao and lista[i][0] > nome):
            lista.insert(i, novo_convocado)
            inserido = True
            break
    
    # Se não foi inserido, adiciona ao final
    if not inserido:
        lista.append(novo_convocado)
    
    print(lista)  # Mostra a lista atualizada, pode ser removido se não necessário

# Testes
l = [('Alisson', 0), ('Marquinhos', 0), ('Casemiro', 1), ('Neymar', 2)]
atualiza_convocados(l, ('Gabigol', 2))  # Deve atualizar a lista
assert l == [('Alisson', 0), ('Marquinhos', 0), ('Casemiro', 1), ('Gabigol', 2), ('Neymar', 2)]

# Testando com um novo convocado que deve ser inserido em ordem alfabética
atualiza_convocados(l, ('Pedro', 2))  # Deve inserir Pedro antes de Neymar
assert l == [('Alisson', 0), ('Marquinhos', 0), ('Casemiro', 1), ('Gabigol', 2), ('Pedro', 2), ('Neymar', 2)]



# def atualiza_convocados(lista, novo_convocado):
#     lista.append(novo_convocado)
#     ult = lista[-1][1]
#     if ult == 0:
#         for i in range(len(lista)-1,-1,-1):
#             if lista[i][1] < lista[i-1][1]:
#                 lista[i-1], lista[i] = lista[i-1], lista[i]
#     if ult == 2:
#         for i in range(len(lista)-1,-1,-1):
#             if lista[i-1][1] > lista[i][1]:
#                 lista[i-1], lista[i] = lista[i-1], lista[i]
#     if ult == 1:
#         for i in range(len(lista)-1,-1,-1):
#             if lista[i][1] < lista[i-1][1]:
#                 lista[i-1], lista[i] = lista[i-1], lista[i]
#     print(lista)


# l = [('Alisson', 0), ('Marquinhos', 0), ('Casemiro', 1), ('Neymar', 2)]
# assert atualiza_convocados(l, ('Gabigol', 2)) == None
# assert l == [('Alisson', 0), ('Marquinhos', 0), ('Casemiro', 1), ('Gabigol', 2),('Neymar', 2)]

# # Lista de Convocados

# Na convocação da Seleção Brasileira, o técnico Tite chegou a
# preparar uma lista de 55 jogadores que ele observou durante os
# últimos 4 anos. Dessa lista de 55 jogadores, Tite escolheu os 26
# que agora estão participando da Copa no Catar.

# Vamos escrever um programa que ajuda a montar a lista de
# convocados. Essa lista, mantida em ordem (por posição e ordem
# alfabética), é aumentada sempre que um novo jogador agrada ao
# técnico. Assim, ele vai montando a lista de forma incremental mas
# mantendo-a organizada. 

# Para facilitar o técnico divide os convocados em 3 posições:
# defesa (representada pelo 0), meio de campo (representado pelo 1)
# e ataque (representado pelo 2). Veja a seguinte lista de
# convocados abaixo:

# ```
# l = [('Alisson', 0), ('Marquinhos', 0), ('Casemiro', 1), ('Neymar', 2)]
# ```

# A lista do exemplo acima já contém dois jogadores de defesa, um meio-campista e um
# atacante. Percebam que a lista é organizada com os jogadores de
# defesa, seguidos de jogadores de meio de campo e, por fim, os
# jogadores de ataque. Os jogadores de mesma posição estão
# ordenados alfabeticamente. Caso o técnico queira inserir o
# atacante Gabigol, a lista ficaria assim:

# ```
# l = [('Alisson', 0), ('Marquinhos', 0), ('Casemiro', 1), ('Gabigol', 2),('Neymar', 2)]
# ```


# Escreva a função `atualiza_convocados(lista, novo_convocado)` que 
# recebe uma lista ordenada de (jogadores, posição) 
# e um novo jogador/posição a ser inserido na
# lista mantendo-a organizada.

# ## ATENÇÃO

# Não é permitido usar nenhum método que faz ordenação em Python.

