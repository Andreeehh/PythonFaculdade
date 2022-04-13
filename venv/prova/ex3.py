n1 = int(input("N1"))
n2 = int(input("N2"))
if (n2 < n1):
    print("N2 deve ser maior que n1")
soma = 0
while n1 < n2:
    n1 = n1 + 1
    if n1 != n2:
        soma = soma + n1
print("Somataria = " + str(soma))