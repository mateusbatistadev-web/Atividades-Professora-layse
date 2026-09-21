def blackjack(a, b, c):
    soma = a + b + c

    if soma <= 21:
        return soma

    if 11 in (a, b, c):
        soma -= 10

    if soma <= 21:
        return soma

    return -1

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

print("Resultado:", blackjack(n1, n2, n3))
