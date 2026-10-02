produtos = {
    1: "Notebook",
    2: "Mouse",
    3: "Teclado"
}

def buscar_produto(id):
    try:
        produto = produtos[id]

        return {
            "status": 200,
            "produto": produto
        }

    except KeyError:
        return {
            "status": 404,
            "mensagem": "Produto não encontrado."
        }

    except Exception:
        return {
            "status": 500,
            "mensagem": "Erro interno do servidor."
        }

id_produto = int(input("Digite o ID do produto: "))

print(buscar_produto(id_produto))
