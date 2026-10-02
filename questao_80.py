class ProdutoInvalidoError(Exception):
    pass

class ValorInvalidoError(Exception):
    pass

class QuantidadeInvalidaError(Exception):
    pass

def registrar_venda(produto, preco, quantidade):
    if produto.strip() == "":
        raise ProdutoInvalidoError("O nome do produto não pode ser vazio.")

    if preco <= 0:
        raise ValorInvalidoError("O preço deve ser maior que zero.")

    if not isinstance(quantidade, int) or quantidade <= 0:
        raise QuantidadeInvalidaError(
            "A quantidade deve ser um número inteiro positivo."
        )

    total = preco * quantidade

    return {
        "produto": produto,
        "preco": preco,
        "quantidade": quantidade,
        "total": total
    }

def gerar_relatorio(vendas):
    if len(vendas) == 0:
        print("Nenhuma venda foi registrada.")
        return

    quantidade_vendas = len(vendas)
    faturamento = 0
    produtos = {}

    for venda in vendas:
        faturamento += venda["total"]
        produto = venda["produto"]
        quantidade = venda["quantidade"]

        if produto in produtos:
            produtos[produto] += quantidade
        else:
            produtos[produto] = quantidade

    produto_mais_vendido = max(produtos, key=produtos.get)
    ticket_medio = faturamento / quantidade_vendas

    print("\n===== RELATÓRIO =====")
    print("Quantidade de vendas:", quantidade_vendas)
    print("Produto mais vendido:", produto_mais_vendido)
    print("Faturamento total: R$", faturamento)
    print("Ticket médio: R$", ticket_medio)

vendas = []

try:
    while True:
        produto = input("\nDigite o nome do produto ou 'fim' para encerrar: ")

        if produto.lower() == "fim":
            break

        try:
            preco = float(input("Digite o preço unitário: "))
            quantidade = int(input("Digite a quantidade vendida: "))

            venda = registrar_venda(produto, preco, quantidade)

        except ProdutoInvalidoError as erro:
            print("Erro:", erro)

        except ValorInvalidoError as erro:
            print("Erro:", erro)

        except QuantidadeInvalidaError as erro:
            print("Erro:", erro)

        except ValueError:
            print("Digite valores numéricos válidos.")

        else:
            vendas.append(venda)
            print("Venda registrada com sucesso!")

        finally:
            print("Operação finalizada.")

finally:
    gerar_relatorio(vendas)
