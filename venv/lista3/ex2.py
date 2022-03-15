n = int(input("Quantos n deseja inserir?\n"))
s = 0
for x in range (0,n):
    s = s + (int(input("Digite um numero para somar:\n"))**2)
print("Soma dos quadrados dos n inseridos = " + str(s))