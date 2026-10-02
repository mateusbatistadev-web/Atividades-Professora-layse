class SaldoInsuficienteError(Exception):
    pass

def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente.")

    return saldo - valor

saldo = 1000

try:
    valor = float(input("Digite o valor do saque: "))
    novo_saldo = sacar(saldo, valor)

    print("Saque realizado.")
    print("Novo saldo:", novo_saldo)

except SaldoInsuficienteError as erro:
    print(erro)
