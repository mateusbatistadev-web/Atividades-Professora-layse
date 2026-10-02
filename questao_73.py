precos = ["100", "50.5", "200", "abc"]

for valor in precos:
    try:
        preco = float(valor)

    except ValueError:
        print("Valor inválido:", valor)

    else:
        desconto = preco * 0.90
        print("Preço com desconto:", desconto)
