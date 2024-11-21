def rotdir(array):
    if len(array) != 0:
        ult = array[-1]
        for i in range(len(array)-1, -1, -1):
            array[i] = array[i-1]
        array[0] = ult
        print(array)
# Rotaciona Array

# Escreva a função `rotdir(array)` que faz uma rotação circular dos elementos do array uma posição à direita. A rotaçao circular consiste em deslocar todos os elementos uma posição à direita, exceto o último que deve passar à primeira posição do array.

# Por exemplo, se o array dado contém os valores: 10, 5, 6, 8, 1, depois de ser rotacionado, irá conter os elementos 1, 10, 5, 6, 8.

# > Importante. Embora `array` seja, de fato, uma lista Python,
# > você deve tratá-lo como um array. Portanto, você deve se
# > restringir às operações características da API de arrays.

    
valores = []
rotdir(valores)
assert valores == []

valores = [10]
rotdir(valores)
assert valores == [10]

valores = [10, 20]
rotdir(valores)
assert valores == [20, 10]

valores = [10, 20, 14, 17, 22, 9, 32]
rotdir(valores)
assert valores == [32, 10, 20, 14, 17, 22, 9]
