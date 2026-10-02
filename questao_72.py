def parse_cpf(cpf):
    if len(cpf) != 11 or not cpf.isdigit():
        raise ValueError("CPF inválido.")

    return cpf

def main():
    cpf = input("Digite o CPF: ")

    try:
        resultado = parse_cpf(cpf)
        print("CPF válido:", resultado)

    except ValueError as erro:
        print("Erro:", erro)

main()
