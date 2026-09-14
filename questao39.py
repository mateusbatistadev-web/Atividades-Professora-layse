import random
numero = random.randint(1, 10)
tentativa = int(input("Adivinhe o número: "))
if tentativa == numero:
    print("Acertou!")
else:
    print("Errou!")
