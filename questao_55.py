disciplinas = ("Matemática", "Português")

alunos = {}

quantidade = int(input("Quantos alunos deseja cadastrar? "))

for i in range(quantidade):
    nome = input("Nome do aluno: ")
    matematica = float(input("Nota de Matemática: "))
    portugues = float(input("Nota de Português: "))

    media = (matematica + portugues) / 2

    if media >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    alunos[nome] = {
        "Matemática": matematica,
        "Português": portugues,
        "Média": media,
        "Situação": situacao
    }

print("\nDisciplinas:", disciplinas)

for nome, dados in alunos.items():
    print("\nAluno:", nome)
    print("Matemática:", dados["Matemática"])
    print("Português:", dados["Português"])
    print("Média:", dados["Média"])
    print("Situação:", dados["Situação"])
