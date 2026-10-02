try:
    lucro = float(input("Digite o lucro do trimestre: "))
    acionistas = int(input("Digite a quantidade de acionistas: "))

    divisao = lucro / acionistas

except ZeroDivisionError:
    print("A quantidade de acionistas não pode ser zero.")

except ValueError:
    print("Digite apenas valores numéricos.")

else:
    print("Cada acionista receberá:", divisao)
