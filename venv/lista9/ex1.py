qA = int(input("Digite a quantidade de alunos"))
alunos = {}
for i in range (qA):
    nome = input("Digite o nome do aluno")
    qN = int(input("Digite a quantidades de notas do aluno a serem inseridas"))
    listaNotas = []
    for n in range (qN):
        listaNotas.append(int(input("Digite a nota do aluno:")))
    alunos[nome] = listaNotas
    print(alunos[nome])
print(alunos)