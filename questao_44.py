matriz = [
    [10, 25, 7],
    [32, 15, 8],
    [4, 50, 12]
]

menor = matriz[0][0]

for linha in matriz:
    for valor in linha:
        if valor < menor:
            menor = valor

print("Menor valor:", menor)
