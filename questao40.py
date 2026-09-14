import random
numero = random.randint(1, 10)
while True:
    tentativa = int(input("Digite um número: "))
    if tentativa == numero:
        print("Acertou!")
        break
    if tentativa < numero:
        print("O número é maior.")
    else:
        print("O número é menor.")
