import traceback

def processar_dados(dados):
    for item in dados:
        try:
            resultado = float(item) * 2
            print("Resultado:", resultado)

        except (TypeError, ValueError):
            print("Erro ao processar:", item)
            traceback.print_exc()

dados = [10, "20", "abc", None, 5]

processar_dados(dados)
