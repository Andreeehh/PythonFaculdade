nomes = []
medias = []
leitura = open("C:\\Users\\andre\\Desktop\\faculdade\\talon\\python\\alunos.txt")
for nome in leitura:
    nome = nome.replace("\n", "")
    nomes.append(nome)
leitura.close()
leitura2 = open("C:\\Users\\andre\\Desktop\\faculdade\\talon\\python\\notas.txt")
for nota in leitura2:
    nota = nota.replace("\n", "")
    nota = nota.split(",")
    notaInt = list(map(int, nota))
    medias.append(sum(notaInt)/len(notaInt))
leitura2.close()
print(nomes)
print(medias)
escrita = open("C:\\Users\\andre\\Desktop\\faculdade\\talon\\python\\medias.txt", "w")
for i in range(len(nomes)):
    escrita.write(nomes[i]+ " média = " + str(medias[i]) + "\n")
escrita.close()
