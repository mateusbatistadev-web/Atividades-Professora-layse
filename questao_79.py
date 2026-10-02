def cadastrar_produto(nome, preco, quantidade):
    if nome.strip() == "":
        raise ValueError("O nome não pode ser vazio.")

    if preco <= 0:
        raise ValueError("O preço deve ser maior que zero.")

    if quantidade < 0:
        raise ValueError("A quantidade não pode ser negativa.")

    return "Produto cadastrado com sucesso."

try:
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço: "))
    quantidade = int(input("Digite a quantidade: "))

    print(cadastrar_produto(nome, preco, quantidade))

except ValueError as erro:
    print("Erro:", erro)
