def verificar_numeros(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

print("Resultado:", verificar_numeros(n1, n2))
