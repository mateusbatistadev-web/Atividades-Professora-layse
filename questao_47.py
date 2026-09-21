matriz = [
    [-2, 5, 8],
    [4, -1, 7],
    [3, 6, -9]
]

quantidade = 0

for linha in matriz:
    for valor in linha:
        if valor > 0:
            quantidade += 1

print("Quantidade de valores positivos:", quantidade)
