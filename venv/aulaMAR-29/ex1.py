notas = []
n = int(input("Digite a quantidade de notas"))
for i in range (n):
    notas.append(int(input("Digite uma nota")))
avg = sum(notas) / len(notas)
dif = []
for i in range (n):
    dif.append(abs(notas[i] - avg))
indice = dif.index(min(dif))
print(str(avg))
print(str(dif))
print(indice)
print(str(notas[indice]))