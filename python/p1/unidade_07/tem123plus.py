def tem123plus(l):
    contador3,contador2, contador1 = 0, 0, 0
    lista = []
    um, dois, tres = 0, 0, 0
    for i in range(len(l) -1, -1, -1):
        if l[i] ==  3:
            contador3 += 1
            if contador3 == 1:
                tres = i
        if l[i] == 2:
            contador2 += 1
            if contador2 == 1:
                dois = i
        if l[i] == 1:
            contador1+=1
            um = i
    #print(um, dois, tres)

    if contador1 > 0 and contador2 > 0 and contador3 > 0 :
        if um < dois < tres:
            return um
        else:
            return -1
    else:
        return -1
assert tem123plus([1, 2]) == -1
assert tem123plus([1, 2, 3, 1, 2, 3]) == 0
assert tem123plus([3, 2, 1]) == -1
assert tem123plus([3, 2, 1, 2, 3]) == 2
assert tem123plus([4, 1, 1, 1, 4, 2, 3]) == 1
assert tem123plus([1, 2, 2, 3]) == 0
assert tem123plus([1, 2, 2, 4]) == -1

# Escreva a função `tem123plus(l)` que recebe uma lista de inteiros
# e verifica se ela contém a subsequência 1, …, 2, …, 3. Observe que
# os três elementos não precisam ser vizinhos mas devem aparecer na
# ordem indicada. Em caso afirmativo, a função deve retornar o
# índice do número 1 na primeira ocorrência da sequencia. Caso
# não haja a sequência na lista, a função deve retornar -1. 


# def tem123plus(l):
#     contador3,contador2, contador1 = 0, 0, 0
#     for i in range(len(l) -1, -1, -1):
#         if l[i] ==  3:
#             contador3 += 1
#         if l[i] == 2:
#             contador2 += 1
#         if l[i] == 1:
#             contador1+=1
#             um = i
#     if contador1 > 0 and contador2 > 0 and contador3 > 0:
#         return um
#     else:
#         return -1




# assert tem123plus([3, 2, 1, 2, 3]) == 2
# assert tem123plus([4, 1, 1, 1, 4, 2, 3]) == 1
# assert tem123plus([1, 2, 2, 3]) == 0
# assert tem123plus([1, 2, 2, 4]) == -1
