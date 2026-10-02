try:
    arquivo = open("relatorio_vendas.txt", "r")
    conteudo = arquivo.read()
    print(conteudo)

except FileNotFoundError:
    print("O arquivo não foi encontrado.")

finally:
    print("Encerrando operação com o arquivo.")
