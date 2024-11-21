def ajeita_array(array):
    n = len(array)
    
    # Passo 1: Separar pares e ímpares
    num_pares = 0
    for i in range(n):
        if array[i] % 2 == 0:
            array[num_pares], array[i] = array[i], array[num_pares]
            num_pares += 1
    
    # Passo 2: Ordenar pares em ordem decrescente
    for i in range(num_pares):
        for j in range(i + 1, num_pares):
            if array[i] < array[j]:
                array[i], array[j] = array[j], array[i]
    
    # Passo 3: Ordenar ímpares em ordem crescente
    for i in range(num_pares, n):
        for j in range(i + 1, n):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

# Exemplo de uso
arr1 = [3, 2, 1, 4, 5, 6, 7, 8, 9]
ajeita_array(arr1)
print(arr1)  # Saída esperada: [8, 6, 4, 2, 1, 3, 5, 7, 9]


# def ordena_par(array):
#     i = 0
#     for i in range(len(array)):
#         for j in range(0, len(array)-1-i):
#             if array[j] < array[j+1] and array[j+1] % 2 == 0:
#                 array[j+1], array[j] = array[j], array[j+1]


# def ordena_impar(array):
#     for i in range(len(array)):   
#         for j in range(0, len(array)-1-i):
#             if array[j] > array[j+1] and array[j] % 2 != 0:
#                 array[j+1], array[j] = array[j], array[j+1]

# def ajeita_array(array):
#     ordena_par(array)
#     ordena_impar(array)


#Escreva a função `ajeita_array(array)` que recebe um array de inteiros e o altera de forma a deixar no início todos os números pares em ordem decrescente seguido dos ímpares em ordem crescente.


arr1 = [3, 2, 1, 4, 5, 6, 7, 8, 9]
assert ajeita_array(arr1) == None
assert arr1 == [8, 6, 4, 2, 1, 3, 5, 7, 9]
