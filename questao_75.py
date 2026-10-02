import random

def conectar_api():
    if random.choice([True, False]):
        raise ConnectionError("Falha na conexão.")

    return True

def realizar_conexao():
    for tentativa in range(1, 4):
        try:
            conectar_api()
            print("Conexão realizada com sucesso.")
            return

        except ConnectionError:
            print("Falha na tentativa", tentativa)

    print("Não foi possível realizar a conexão após 3 tentativas.")

realizar_conexao()
