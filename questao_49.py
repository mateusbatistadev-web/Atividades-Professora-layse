alunos = {}

for i in range(5):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota: "))

    alunos[nome] = nota

print("\nRegistros:")

for nome, nota in alunos.items():
    print(nome, "-", nota)
