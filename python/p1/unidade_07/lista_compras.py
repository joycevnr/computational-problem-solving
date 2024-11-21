def adiciona_item(item, lista):
    lista.append(item)
    i = len(lista) -1
    while i > 0 and lista[i-1] > lista[i]:
        lista[i-1], lista[i] = lista[i], lista[i-1]
        i -= 1

    return lista

lista = ['acucar', 'leite', 'paes', 'queijo']
adiciona_item('cafe', lista)
print(lista)
assert lista == ['acucar', 'cafe', 'leite', 'paes', 'queijo']
