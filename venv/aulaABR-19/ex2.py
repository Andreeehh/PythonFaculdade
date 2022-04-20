def sit(nome, nota):
    if nota >= 7:
        return "Aluno " + nome + " aprovado"
    elif nota >= 4:
        return "Aluno " + nome + " de exame"
    else:
        return "Aluno " + nome + " reprovado"
print(sit(input("Digite o nome do aluno"), float(input("Digite a nota do aluno"))))