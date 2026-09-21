alunos = {}
soma = 0

for i in range(5):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota: "))

    alunos[nome] = nota
    soma += nota

media = soma / 5

print("\nMédia da turma:", media)

print("\nAlunos aprovados:")

for nome, nota in alunos.items():
    if nota >= 7:
        print(nome)
