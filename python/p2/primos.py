def ehPrimo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def primosGemeos():
    primos = []
    for j in range(2, 1000):
        if ehPrimo(j):
            primos.append(j)

    gemeos = [(primos[i], primos[i+1]) for i in range(len(primos) - 1) if primos[i+1] - primos[i] == 2]

    for par in gemeos:
        print(par)
    print(f"Total de pares de primos gêmeos: {len(gemeos)}")

primosGemeos()
