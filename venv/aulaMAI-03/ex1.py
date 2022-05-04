n = int(input("N: "))
# modo:r(read/default),w(write),a(append) ou+(atualização)
escrita = open("C:\\Users\\andre\\Desktop\\faculdade\\talon\\python\\reais.txt.txt", "w")
for i in range(n):
    real = float(input("Nro Real: "))
    escrita.write(str(real) + "\n")
escrita.close()
leitura = open("C:\\Users\\andre\\Desktop\\faculdade\\talon\\python\\reais.txt.txt")
for real in leitura:
    print(float(real))
leitura.close()
leitura = open("C:\\Users\\andre\\Desktop\\faculdade\\talon\\python\\reais.txt.txt")
real = leitura.readline()
while real:
    print(float(real))
    real = leitura.readline()
leitura.close()
