def pivot(numeros):
    if len(numeros) == 0:
        return  # Lista vazia, não há o que fazer

    pivot = numeros[0]  # Escolhemos o primeiro elemento como pivot
    pos = 0  # O índice do último elemento menor que o pivot
    
    # Iteramos sobre a lista a partir do segundo elemento
    for i in range(1, len(numeros)):
        if numeros[i] < pivot:
            pos += 1
            # Trocamos o elemento menor com o que está na posição 'pos'
            numeros[i], numeros[pos] = numeros[pos], numeros[i]
    
    # Finalmente, colocamos o pivot em seu lugar correto
    numeros[0], numeros[pos] = numeros[pos], numeros[0]

# Exemplo de uso
numeros = [6, 4, 8, 1, 7, 3]
pivot(numeros)
print(numeros)  
assert sorted(numeros[:3]) == [1, 3, 4]  # Menores que o pivot
assert sorted(numeros[3:]) == [6, 7, 8]  # Maiores que o pivot