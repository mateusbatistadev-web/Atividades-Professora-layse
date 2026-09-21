import random

numero = random.randint(1, 10)

while True:
    tentativa = int(input("Digite seu palpite: "))

    if tentativa == numero:
        print("Você acertou!")
        break
    elif tentativa < numero:
        print("O número procurado é maior.")
    else:
        print("O número procurado é menor.")
