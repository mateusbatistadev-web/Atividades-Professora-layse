def calcular_gorjeta(conta):
    gorjeta = conta * 0.10
    return gorjeta

valor = float(input("Digite o valor da conta: "))

gorjeta = calcular_gorjeta(valor)

print("Gorjeta:", gorjeta)
