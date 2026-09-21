def numero_perfeito(numero):
    soma = 0

    for i in range(1, numero):
        if numero % i == 0:
            soma += i

    return soma == numero

numero = int(input("Digite um número: "))

if numero_perfeito(numero):
    print("O número é perfeito.")
else:
    print("O número não é perfeito.")
