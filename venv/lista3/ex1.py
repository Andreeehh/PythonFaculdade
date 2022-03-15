n = int(input("Digite um valor: \n"))
i = 1
while i * (i+1) * (i+2) < n:
    i = i + 1
if (i * (i+1) * (i+2)) == n:
    print("É um número triangular")
    print("%d eh o produto %d*%d*%d" %(n,i,i+1,i+2))
else:
    print("Não é um numero triangular")