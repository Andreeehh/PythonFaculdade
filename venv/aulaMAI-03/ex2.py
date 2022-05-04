n = int(input("N: "))
# modo:r(read/default),w(write),a(append) ou+(atualização)
nome = []
sobrenome = []
nomeCompleto = []
def escreve(n, string, fileName):
    escrita = open("C:\\Users\\andre\\Desktop\\faculdade\\talon\\python\\"+ fileName + ".txt", "w")
    for i in range(n):
        escrita.write(str(string[i]) + "\n")
    escrita.close()
for i in range(n):
    nome.append(input("Digite o nome: "))
    sobrenome.append(input("Digite o sobrenome: "))
    nomeCompleto.append(nome[i] + " " + sobrenome[i])
escreve(n, nome, "nome")
escreve(n, sobrenome,"sobrenome")
escreve(n, nomeCompleto,"nome_completo")
