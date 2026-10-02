def calcular_media(n1, n2, n3):
    notas = [n1, n2, n3]

    for nota in notas:
        if nota < 0 or nota > 10:
            raise ValueError("A nota deve estar entre 0 e 10.")

    return sum(notas) / 3

try:
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))

    media = calcular_media(n1, n2, n3)

    print("Média:", media)

    if media >= 7:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

except ValueError as erro:
    print("Erro:", erro)
